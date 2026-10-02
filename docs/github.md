# GitHub Wiki and releases

## Documentation layout

- `README.md` introduces the project.
- `docs/README.md` indexes the documentation.
- The GitHub Wiki points readers to repository files.
- GitHub Releases records published versions and release notes.

Keep detailed documentation in the main repository so it is reviewed and
versioned with the code. The Wiki navigation templates live under `docs/wiki/`;
update those files before synchronizing the Wiki. Links to `main` show the latest
documentation. To read a specific version, browse the corresponding release tag.

## Initialize or update the Wiki

The target is the private repository
[`latifo01/governance-brain`](https://github.com/latifo01/governance-brain).
Confirm that **Settings → General → Features → Wikis** is enabled. If the Wiki
has never been initialized, create its first `Home` page through the GitHub Wiki
interface before cloning its separate Git repository.

To synchronize the navigation pages on Ubuntu/WSL, run from the main repository
root after installing and authenticating GitHub CLI:

```sh
gh auth setup-git
git clone https://github.com/latifo01/governance-brain.wiki.git ../governance-brain-wiki
cp docs/wiki/Home.md docs/wiki/_Sidebar.md ../governance-brain-wiki/
git -C ../governance-brain-wiki status --short
git -C ../governance-brain-wiki diff --check
git -C ../governance-brain-wiki diff
```

For an existing clone, pull its current branch with `git pull --ff-only` before
copying the pages. Inspect existing pages before replacing them. Once the exact
Wiki diff is approved for publication:

```sh
git -C ../governance-brain-wiki add Home.md _Sidebar.md
git -C ../governance-brain-wiki commit -m "docs: organize wiki navigation"
git -C ../governance-brain-wiki push
```

On Windows, replace the copy command with:

```powershell
Copy-Item docs/wiki/Home.md, docs/wiki/_Sidebar.md -Destination ../governance-brain-wiki/
```

The Wiki uses its own Git history. Publishing main-repository files does not
automatically synchronize it. Keep the Wiki focused on navigation to reviewed
documentation rather than copying source originals, evidence quotes or ingest.

## Version history through GitHub Releases

Use [GitHub Releases](https://github.com/latifo01/governance-brain/releases) as
the version history. Include:

- a concise release summary;
- additions, changes and fixes since the previous release;
- migration or setup instructions when needed;
- known limitations and evidence or coverage gaps;
- relevant validation results and links to documentation for that tag.

For the first release, use **Releases → Draft a new release**, select the exact
already-pushed v1 commit, choose its tag (for example `v1.0.0`) and review the
notes before publishing. GitHub can generate a starting draft from merged pull
requests; supplement it with the initial scope and known limitations.

For later releases with an existing tag, GitHub CLI can prepare a draft:

```sh
gh release create <existing-tag> --repo latifo01/governance-brain \
  --verify-tag --draft --generate-notes --title "Governance Brain <existing-tag>"
```

Replace the placeholders with the reviewed tag. `--verify-tag` requires that
tag to already exist remotely. Review generated notes before publishing, and
attach only the sharing artefacts authorized for the target repository.

A GitHub release records a software or documentation version. Knowledge
publication still follows the independent review and hash-bound human approval
workflow in [WORKSHOP.md](../WORKSHOP.md).
