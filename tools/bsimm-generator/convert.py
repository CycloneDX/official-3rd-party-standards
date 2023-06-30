import csv
import json

csv_file = 'raw.githubusercontent.com_rtxsecurity_bsimm13-parsable_rtxmono_bsimm13.csv'  # Replace with the path to your CSV file

# Define the JSON structure
json_structure = {
    "requirements": []
}

# Read the CSV file and populate the JSON structure
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        if row[0] == "SM":
            parent = "governance-sm"
        elif row[0] == "CP":
            parent = "governance-cp"
        elif row[0] == "T":
            parent = "governance-t"
        elif row[0] == "AM":
            parent = "intelligence-am"
        elif row[0] == "SDF":
            parent = "intelligence-sdf"
        elif row[0] == "SR":
            parent = "intelligence-sr"
        elif row[0] == "AA":
            parent = "ssdl-touchpoints-aa"
        elif row[0] == "CR":
            parent = "ssdl-touchpoints-cr"
        elif row[0] == "ST":
            parent = "ssdl-touchpoints-st"
        elif row[0] == "PT":
            parent = "deployment-pt"
        elif row[0] == "SE":
            parent = "deployment-se"
        elif row[0] == "CMVM":
            parent = "deployment-cmvm"

        requirement = {
            "bom-ref": row[0] + row[1] + "." + row[2],
            "identifier": row[0] + row[1] + "." + row[2],
            "title": row[4],
            "text": row[5],
            "parent": parent
        }
        json_structure["requirements"].append(requirement)

# Convert the JSON structure to a JSON string
json_string = json.dumps(json_structure, indent=4)

# Print the JSON string
print(json_string)
