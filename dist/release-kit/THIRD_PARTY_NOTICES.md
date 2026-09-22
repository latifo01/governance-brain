# Licensing and redistribution

`LICENSE` applies to original project code contributed under Apache-2.0. It does
not relicense documents, datasets, standards, source extracts, or third-party
text in notes. Dependency packages retain their respective licenses and are
restored separately with `uv`; they are not vendored in the release kit.

Original project operating instructions are included to permit reconstruction.
The explicit list in `config/redistribution-policy.json` selects public kit
files. Source originals, ingest units, proposal and review bodies, local provider
settings, and prior Git history are excluded. Source IDs, hashes, adapters and
unit locators in the generated seed preserve identity; they grant no rights to
the underlying documents and imply no review or publication approval.

Knowledge-note redistribution defaults to **deny**. An exact-file grant records
the path, SHA-256, permission `redistribute`, applicable license, and review record.
A changed note requires a new grant. Public release preparation must review
these decisions and source acquisition rights before any push or publication.

The private CDO continuation snapshot is a separate, operator-authorized
transfer to `github.com/latifo01/governance-brain` with private visibility. It
may contain the exact source and ingest files covered by
`config/private-handoff-policy.json`. Public availability of a document is not
represented as a public redistribution licence. The private authorization does
not permit making the repository public, publishing an OKF bundle, or
relicensing third-party documents.

The Open Knowledge Format mapping references the public specification maintained
by GoogleCloudPlatform. This project does not vendor its specification text.
Source and specification attributions are retained in `docs/okf-mapping.md` and
the generated bundle manifest. OKF compatibility is a format claim, not an
endorsement or evidence of legal correctness.
