# NIST SSDF Standard Generation

Generate a CycloneDX Attestation for the NIST Secure Software Development Framework (SSDF).

## Requirements

- Install `python 3.10`, `poetry`, and `curl`

## Running

- `./generate.sh`

## Output

This will product a CycloneDX Attestation File containing the NIST SSDF
Standard only. `attestations`, `claims`, and other fields of the spec 
can then be filled out to show compliance to the SSDF.

