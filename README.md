# Official Third‑Party Standards & Requirements
This repository contains official third-party standards that have been transformed into CycloneDX v1.6 requirements.
These requirements are intended to document compliance to a standard in a machine readable format that is consistent with
the CycloneDX specification.

---

## What is this repository?

| &nbsp;       | &nbsp;                                                                                                                                                                                                                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**  | Provide a single, machine‑readable catalogue of well‑known open standards that have been mapped into the [CycloneDX v1.6](https://cyclonedx.org/) *requirements* model.                                                                                                                         |
| **Why**      | • Enables tool‑chains to import a standard **as a BOM**, verify controls automatically, and report compliance.<br>• Eliminates one‑off parsers for every PDF, spreadsheet or bespoke XML format.<br>• Keeps the source of truth under version control so updates are transparent and traceable. |
| **Audience** | Security engineers, compliance teams, CycloneDX ecosystem tools, CI/CD pipelines.                                                                                                                                                                                                               |

---

## Repository layout

```text
standards/
├─ <Publisher>/
│  └─ <Standard‑Name>/
│     └─ <file>.cdx.json   # CycloneDX requirement BOMs
└─ feed.json               # JSON Feed 1.1 catalogue (auto‑generated)
```

## The catalogue feed (`standards/feed.json`)

* **Format:** [JSON Feed 1.1](https://www.jsonfeed.org/version/1.1) with a small CycloneDX extension.
* **Deployed URL:** [https://cyclonedx.org/standards/feed.json](https://cyclonedx.org/standards/feed.json)

## Contributing a new standard
Create standards/<Publisher>/<Standard‑Name>/.

Add the CycloneDX requirement BOM as <standard>-<version>.cdx.json.

Open a pull request.

Once merged, the feed updates automatically.

## License & usage
### Repository
The scripts, workflow files, and overall repository structure are licensed under the
Apache License 2.0. See LICENSE for details.

### Individual standards
Each standard included here retains the license designated by its original publisher.
That license is declared inside the corresponding *.cdx.json file (usually in `metadata.licenses`).
Before redistributing or embedding a particular standard, review and comply with the terms in that file.
