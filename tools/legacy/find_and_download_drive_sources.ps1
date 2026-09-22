param(
    [string]$ManifestPath = (Join-Path $PSScriptRoot 'drive_sources_manifest.csv'),
    [string]$OutputDir = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputDir)
$resolvedManifest = [System.IO.Path]::GetFullPath($ManifestPath)
if (-not (Test-Path -LiteralPath $resolvedManifest -PathType Leaf)) {
    throw "Manifest not found: $resolvedManifest"
}
if (-not (Test-Path -LiteralPath $resolvedOutput -PathType Container)) {
    throw "Output directory not found: $resolvedOutput"
}

function ConvertFrom-DdgRedirect {
    param([string]$Href)
    $decoded = [System.Net.WebUtility]::HtmlDecode($Href)
    if ($decoded.StartsWith('//')) { $decoded = 'https:' + $decoded }
    if ($decoded -match '[?&]uddg=([^&]+)') {
        return [uri]::UnescapeDataString($Matches[1])
    }
    return $decoded
}

function Get-SearchResults {
    param([string]$Query)
    $encoded = [uri]::EscapeDataString($Query)
    $uri = "https://lite.duckduckgo.com/lite/?q=$encoded"
    try {
        $response = Invoke-WebRequest -UseBasicParsing -Uri $uri -Headers @{'User-Agent'='Mozilla/5.0'} -TimeoutSec 45
        $pattern = '(?is)<a\s+rel=["'']nofollow["'']\s+href=["''](?<u>[^"'']+)["'']\s+class=["'']result-link["'']>(?<t>.*?)</a>'
        $matches = [regex]::Matches($response.Content, $pattern)
        $items = foreach ($match in $matches) {
            $title = [regex]::Replace($match.Groups['t'].Value, '<[^>]+>', '')
            [pscustomobject]@{
                Title = [System.Net.WebUtility]::HtmlDecode($title).Trim()
                Url = ConvertFrom-DdgRedirect $match.Groups['u'].Value
            }
        }
        return @($items)
    }
    catch {
        Write-Warning "Search failed for '$Query': $($_.Exception.Message)"
        return @()
    }
}

function Test-TrustedHost {
    param([string]$Url, [string[]]$TrustedDomains)
    try { $hostName = ([uri]$Url).DnsSafeHost.ToLowerInvariant() } catch { return $false }
    foreach ($domain in $TrustedDomains) {
        $d = $domain.Trim().ToLowerInvariant()
        if ($d -and ($hostName -eq $d -or $hostName.EndsWith('.' + $d))) { return $true }
    }
    return $false
}

function Get-SafeFileName {
    param([string]$Title, [string]$SourceId)
    $name = $Title.Trim()
    foreach ($c in [System.IO.Path]::GetInvalidFileNameChars()) { $name = $name.Replace([string]$c, '_') }
    $name = ($name -replace '\s+', ' ').Trim().TrimEnd('.')
    if (-not $name.ToLowerInvariant().EndsWith('.pdf')) { $name += '.pdf' }
    if ($name.Length -gt 180) { $name = $name.Substring(0, 171).TrimEnd() + '-' + $SourceId.Substring(0, 8) + '.pdf' }
    return $name
}

function Get-PdfLinksFromHtml {
    param([string]$PageUrl, [string]$Html)
    $links = New-Object System.Collections.Generic.List[string]
    $pattern = '(?is)href\s*=\s*["''](?<u>[^"'']+\.pdf(?:\?[^"'']*)?)["'']'
    foreach ($m in [regex]::Matches($Html, $pattern)) {
        try { $links.Add(([uri]::new([uri]$PageUrl, [System.Net.WebUtility]::HtmlDecode($m.Groups['u'].Value))).AbsoluteUri) } catch {}
    }
    return @($links | Select-Object -Unique)
}

function Save-IfPdf {
    param([string]$Url, [string]$TargetPath)
    $tempPath = $TargetPath + '.part'
    if (Test-Path -LiteralPath $tempPath) { Remove-Item -LiteralPath $tempPath -Force }
    try {
        $effectiveUrl = $Url
        if ($effectiveUrl -match '^https://github\.com/.+/blob/') { $effectiveUrl = $effectiveUrl -replace '/blob/', '/raw/' }
        Invoke-WebRequest -UseBasicParsing -Uri $effectiveUrl -Headers @{'User-Agent'='Mozilla/5.0'} -MaximumRedirection 10 -TimeoutSec 90 -OutFile $tempPath
        $stream = [System.IO.File]::OpenRead($tempPath)
        try {
            $bytes = New-Object byte[] 5
            $read = $stream.Read($bytes, 0, 5)
        } finally { $stream.Dispose() }
        $header = [System.Text.Encoding]::ASCII.GetString($bytes, 0, $read)
        if ($header -ne '%PDF-') {
            Remove-Item -LiteralPath $tempPath -Force
            return $false
        }
        $fullTarget = [System.IO.Path]::GetFullPath($TargetPath)
        if (-not $fullTarget.StartsWith($resolvedOutput, [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Unsafe target path: $fullTarget"
        }
        Move-Item -LiteralPath $tempPath -Destination $fullTarget
        return $true
    }
    catch {
        if (Test-Path -LiteralPath $tempPath) { Remove-Item -LiteralPath $tempPath -Force }
        return $false
    }
}

$manifest = Import-Csv -LiteralPath $resolvedManifest
$results = New-Object System.Collections.Generic.List[object]
$index = 0
foreach ($source in $manifest) {
    $index++
    $trusted = @($source.trusted_domains -split ';' | Where-Object { $_ })
    Write-Host "[$index/$($manifest.Count)] $($source.title)"
    $searchResults = Get-SearchResults $source.search_hint
    $trustedResults = @($searchResults | Where-Object { Test-TrustedHost $_.Url $trusted })
    $bestPage = if ($trustedResults.Count) { $trustedResults[0].Url } else { '' }
    $status = 'not_found'
    $downloadUrl = ''
    $localFile = ''

    if ($source.download_allowed -ne 'true') {
        $status = if ($bestPage) { 'official_page_found_not_downloaded' } else { 'official_page_not_found' }
    }
    else {
        $fileName = Get-SafeFileName $source.title $source.source_id
        $targetPath = Join-Path $resolvedOutput $fileName
        if (Test-Path -LiteralPath $targetPath -PathType Leaf) {
            $status = 'already_present'
            $localFile = $targetPath
        }
        else {
            $candidates = New-Object System.Collections.Generic.List[string]
            foreach ($item in $trustedResults) {
                if (-not $candidates.Contains($item.Url)) { $candidates.Add($item.Url) }
                if ($candidates.Count -ge 8) { break }
            }
            $expanded = New-Object System.Collections.Generic.List[string]
            foreach ($candidate in @($candidates)) {
                if ($candidate -match '(?i)\.pdf(?:$|[?#])' -and (Save-IfPdf $candidate $targetPath)) {
                    $status = 'downloaded'
                    $downloadUrl = $candidate
                    $localFile = $targetPath
                    break
                }
                try {
                    $page = Invoke-WebRequest -UseBasicParsing -Uri $candidate -Headers @{'User-Agent'='Mozilla/5.0'} -MaximumRedirection 10 -TimeoutSec 45
                    foreach ($pdfLink in (Get-PdfLinksFromHtml $candidate $page.Content)) {
                        if ((Test-TrustedHost $pdfLink $trusted) -and -not $expanded.Contains($pdfLink)) { $expanded.Add($pdfLink) }
                    }
                } catch {}
            }
            if ($status -ne 'downloaded') {
                foreach ($pdfLink in $expanded) {
                    if (Save-IfPdf $pdfLink $targetPath) {
                        $status = 'downloaded'
                        $downloadUrl = $pdfLink
                        $localFile = $targetPath
                        break
                    }
                }
            }
            if ($status -ne 'downloaded' -and $bestPage) { $status = 'official_page_found_no_public_pdf' }
        }
    }

    $results.Add([pscustomobject]@{
        source_id = $source.source_id
        title = $source.title
        search_query = $source.search_hint
        status = $status
        official_or_best_url = if ($downloadUrl) { $downloadUrl } else { $bestPage }
        local_file = $localFile
    })
    Start-Sleep -Milliseconds 350
}

$csvPath = Join-Path $resolvedOutput 'drive_sources_search_results.csv'
$results | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8
$summary = $results | Group-Object status | Sort-Object Name | Select-Object Name, Count
$summary | Format-Table -AutoSize
Write-Host "Results: $csvPath"
