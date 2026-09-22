$ErrorActionPreference = "Stop"

$workspace = (Resolve-Path -LiteralPath ".").Path
$expected = "C:\Users\abdel\llm wiki - risk"
if ($workspace -ne $expected) {
    throw "Unexpected workspace: $workspace"
}

$sectionFolders = @(
    "01_AI_Auditing",
    "02_AI_Security_Frameworks",
    "03_CoSAI",
    "04_Data_Protection",
    "05_EU_AI_Legislation",
    "06_ISO_Standards_not_downloaded",
    "07_Model_Risk_Management",
    "08_NIST_AI_Risk",
    "09_Operational_Risk_manual",
    "10_Responsible_AI",
    "99_Admin_and_Quarantine"
)

foreach ($folder in $sectionFolders) {
    New-Item -ItemType Directory -Path (Join-Path $workspace $folder) -Force | Out-Null
}

$mapping = @{
    "ai-auditing_checklist-for-ai-auditing-scores_edpb-spe-programme_en.pdf" = "01_AI_Auditing"
    "ai-auditing_proposal-for-ai-leaflets_edpb-spe-programme_en.pdf" = "01_AI_Auditing"
    "ai-auditing_proposal-for-algo-scores_edpb-spe-programme_en.pdf" = "01_AI_Auditing"

    "AIUC-1_ Crosswalks OWASP Top 10 For Agentic Applications.pdf" = "02_AI_Security_Frameworks"
    "Analyse des attaques sur les systèmes de l'IA — Wiki Campus Cyber.pdf" = "02_AI_Security_Frameworks"
    "OWASP GenAl State of Agentic Al Security and Governance.pdf" = "02_AI_Security_Frameworks"
    "OWASP Top 10 for LLM Applications 2026.pdf" = "02_AI_Security_Frameworks"
    "OWASP-Top-10-for-Agentic-Applications-2026-12.6-1.pdf" = "02_AI_Security_Frameworks"

    "CoSAI agentic-identity-and-access-control.pdf" = "03_CoSAI"
    "CoSAI AI-Incident-Response.pdf" = "03_CoSAI"
    "CoSAI AI-Shared-Responsibility-Framework.pdf" = "03_CoSAI"
    "CoSAI Mgf for Agentic AI (atx Release) July 2026.pdf" = "03_CoSAI"
    "CoSAI model-context-protocol-security.pdf" = "03_CoSAI"
    "CoSAI preparing-defenders-of-ai-systems.pdf" = "03_CoSAI"
    "CoSAI risks-and-controls-for-the-ai-supply-chain-v1.pdf" = "03_CoSAI"
    "CoSAI signing-ml-artifacts.pdf" = "03_CoSAI"

    "edpb_guidelines_202401_legitimateinterest_en.pdf" = "04_Data_Protection"
    "edpb_summary_202401_legitimateinterest_en.pdf" = "04_Data_Protection"
    "spe-training-on-ai-and-data-protection-legal_en.pdf" = "04_Data_Protection"

    "2018 GDPR Full text EN.pdf" = "05_EU_AI_Legislation"
    "2024 AI Act OJ_L_202401689_FR_TXT.pdf" = "05_EU_AI_Legislation"
    "2024 FRIA Computer Law & security Review.pdf" = "05_EU_AI_Legislation"
    "2026 EU Digital Omnibus - Annexes.pdf" = "05_EU_AI_Legislation"
    "2026 EU Digital Omnibus.pdf" = "05_EU_AI_Legislation"
    "AI AGENTS UNDER EU LAW A COMPLIANCE ARCHITECTURE FOR AI PROVIDERS.pdf" = "05_EU_AI_Legislation"
    "edpb_opinion_202428_ai-models_en.pdf" = "05_EU_AI_Legislation"
    "Guidelines on prohibited AI practices under AI Act.pdf" = "05_EU_AI_Legislation"
    "Guidelines on the definition of AI System under AI Act.pdf" = "05_EU_AI_Legislation"
    "Guidelines on transparency obligations for certain AI systems under Article 50 of AI Act.pdf" = "05_EU_AI_Legislation"

    "sr1107.pdf" = "07_Model_Risk_Management"
    "sr1107a1.pdf" = "07_Model_Risk_Management"
    "SR2602.pdf" = "07_Model_Risk_Management"

    "NIST AI RMF 1.0.pdf" = "08_NIST_AI_Risk"
    "NIST AI RMF Playbook.pdf" = "08_NIST_AI_Risk"

    "Microsoft Responsible AI Transparency Report.pdf" = "10_Responsible_AI"
    "METR risk-report-feb-mar-2026.pdf" = "10_Responsible_AI"
}

foreach ($fileName in $mapping.Keys) {
    $matches = Get-ChildItem -LiteralPath $workspace -File -Recurse |
        Where-Object {
            $_.Name -eq $fileName -and
            $_.FullName -notlike (Join-Path $workspace "99_Admin_and_Quarantine\*") -and
            $_.FullName -notlike (Join-Path $workspace "_unverified_downloads\*")
        }
    foreach ($match in $matches) {
        $destination = Join-Path (Join-Path $workspace $mapping[$fileName]) $fileName
        if ($match.FullName -ne $destination) {
            Move-Item -LiteralPath $match.FullName -Destination $destination -Force
        }
    }
}

$oldQuarantine = Join-Path $workspace "_unverified_downloads"
$newQuarantineParent = Join-Path $workspace "99_Admin_and_Quarantine"
if (Test-Path -LiteralPath $oldQuarantine) {
    Move-Item -LiteralPath $oldQuarantine -Destination $newQuarantineParent -Force
}

$oldFolders = @(
    "01_EDPB_AI_Auditing",
    "02_AI_Security_Agentic_AI",
    "03_GDPR_Data_Protection_EDPB",
    "04_EU_AI_Act_Digital_Regulation",
    "05_Standards_Risk_Frameworks",
    "06_ORX_Operational_Risk_manual"
)
foreach ($folder in $oldFolders) {
    $path = Join-Path $workspace $folder
    if ((Test-Path -LiteralPath $path) -and -not (Get-ChildItem -LiteralPath $path -Force)) {
        Remove-Item -LiteralPath $path -Force
    }
}

Remove-Item -LiteralPath (Join-Path $workspace "probe_mcp_codex_app_tools.mjs") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "current_screen.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "current_screen_after_activate.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "foreground_after_alttab.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "notebook_current.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "notebook_screen.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "notebook_screen_after_expand.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "notebook_screen_pagedown.png") -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath (Join-Path $workspace "notebook_screen_scroll1.png") -Force -ErrorAction SilentlyContinue
