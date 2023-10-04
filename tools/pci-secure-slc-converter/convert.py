#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' CycloneDX converter class

    Copyright (c) 2023 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import json
from dicttoxml2 import dicttoxml
import datetime
import uuid
import csv
import re

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

csv_file = 'Machine_Readable_Secure_SLC_v1-1.csv'

# Define the JSON structure
json_structure = {
    "requirements": []
}


class CycloneDX:
    bom = {}
    bom['bomFormat'] = "CycloneDX"
    bom['specVersion'] = "1.6"
    bom['serialNumber'] = "urn:uuid:" + str(uuid.uuid4())
    bom['version'] = 1
    bom['metadata'] = {}
    bom['metadata']['timestamp'] = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    bom['metadata']['licenses'] = []
    #bom['metadata']['licenses'].append({})
    #bom['metadata']['licenses'][0]['license'] = {}
    #bom['metadata']['licenses'][0]['license']['id'] = "CC-BY-SA-4.0"
    #bom['metadata']['licenses'][0]['license']['url'] = "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt"
    bom['metadata']['supplier'] = {}
    bom['metadata']['supplier']['name'] = "OWASP Foundation"
    bom['metadata']['supplier']['url'] = [ "https://owasp.org" ]
    bom['definitions'] = {}
    bom['definitions']['standards'] = []
    bom['definitions']['standards'].append({})
    bom['definitions']['standards'][0]['bom-ref'] = "pcissc-sslc-1.1"
    bom['definitions']['standards'][0]['name'] = "PCI Secure Software Lifecycle (Secure SLC) Requirements and Assessment Procedures"
    bom['definitions']['standards'][0]['version'] = "1.1"
    bom['definitions']['standards'][0]['description'] = "PCI Secure SLC provides a baseline of security requirements with corresponding assessment procedures and guidance to help software vendors design, develop, and maintain secure software throughout the software lifecycle."
    bom['definitions']['standards'][0]['owner'] = "PCI Security Standards Council"
    bom_ref_prepend = "pcissc-sslc-" + bom['definitions']['standards'][0]['version']

    def __init__(self):
        with open(csv_file, 'r') as file:
            requirements = []
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            previous_row = None
            y = 0
            for row in csv_reader:
                previous_row = row
                if row[0]:
                    requirements.append(self.convert_requirement(row[0], row[1], row[2], None))
                    y = y + 1
                if row[3]:
                    requirements.append(self.convert_requirement(row[3], None, row[4], row[3]))
                    y = y + 1
                if row[5]:
                    requirements.append(self.convert_requirement(row[5], None, row[6], row[5]))
                    y = y + 1
                if row[7]:
                    requirements[y-1]['descriptions'] = []
                    requirements[y-1]['descriptions'].append({})
                    requirements[y-1]['descriptions'][0] = previous_row[7]

            self.bom['definitions']['standards'][0]['requirements'] = requirements

    def convert_requirement(self, identifier, title, text, parent):
        requirement = {}
        requirement['bom-ref'] = "pcissc-sslc-1.1-" + identifier
        requirement['identifier'] = identifier
        if title:
            requirement['title'] = title
        requirement['text'] = text
        if parent:
            requirement['parent'] = "pcissc-sslc-1.1-" + parent.rsplit('.', 1)[0]
        return requirement

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.bom, indent = 2, sort_keys = False, ensure_ascii=False).strip()


cdx = CycloneDX()
print(cdx.to_json())
