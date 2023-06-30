# BSIMM Generation

Generate a CycloneDX standards and requirements doc for Build Security In Maturity Model (BSIMM).

## Requirements

- Install `python 3.10`
- Download the CSV from https://github.com/rtxsecurity/bsimm13-parsable

## Running

- `python convert.py`

## Output

This will product the "requirements" array. However, the domains and practices are not included in the CSV. They will
need to be manually added.