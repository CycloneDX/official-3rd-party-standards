#!/bin/sh

#curl -o NIST.SP.800-218.SSDF-table.xlsx https://csrc.nist.gov/csrc/media/Publications/sp/800-218/final/documents/NIST.SP.800-218.SSDF-table.xlsx

echo "Installing via poetry"
poetry install

echo "Generating SSDF"
poetry run attestation_generator

echo "Checking json compliance"
cat ssdf-1.1.cdx.json | jq empty

echo "Moving SSDF over to standards folder"
mv ssdf-1.1.cdx.json ../../standards/NIST_SSDF/nist_secure-software-development-framework_1.1.cdx.json