# CISA Secure Software Attestation Form Generation

Generate a CycloneDX Attestation for the CISA Secure Software Attestation Form (SSAF).

## Requirements

- Install `python 3.10` and `poetry`

## Running

- `./generate.sh`

## Output

This will product a CycloneDX Attestation File containing the CISA SSAF
only. `attestations`, `claims`, and other fields of the spec 
can then be filled out to show compliance to the SSDF.

