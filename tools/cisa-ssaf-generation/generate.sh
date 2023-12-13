#!/bin/sh

#curl -o NIST.SP.800-218.SSDF-table.xlsx https://csrc.nist.gov/csrc/media/Publications/sp/800-218/final/documents/NIST.SP.800-218.SSDF-table.xlsx

echo "Installing via poetry"
poetry install

echo "Generating SSDF"
poetry run attestation_generator

echo "Checking json compliance"
cat ssaf-DRAFT-2023-11.cdx.json | jq empty

echo "Moving SSAF over to standards folder"
mv ssaf-DRAFT-2023-11.cdx.json ../../standards/CISA/SSAF