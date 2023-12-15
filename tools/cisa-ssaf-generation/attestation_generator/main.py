"""
Python module that reads in the NIST SSDF and will generate
the CycloneDX Attestation for the standard.
"""

from uuid import uuid4
from yaml import safe_load

from jinja2 import Environment, FileSystemLoader

class Standard:  # pylint: disable=too-few-public-methods
    """
    Class containing SSDF "standards" metadata
    """

    def __init__(self):
        self.identifier = "ssaf-DRAFT-2023-11"
        self.name = "Secure Software Development Attestation Form"
        self.description = "This self-attestation form identifies the minimum secure software development requirements a software producer must meet, and attest to meeting, before software subject to the requirements of M-22-18 and M-23-16 may be used by Federal agencies. This form is used by software producers to attest that the software they produce is developed in conformity with specified secure software development practices."
        self.version = "DRAFT-2023-11"
        self.owner = "Cybersecurity and Infrastructure Security Agency"
        self.url = "https://www.cisa.gov/sites/default/files/2023-11/Secure%20Software%20Development%20Attestation%20Form_508c.pdf"  # pylint: disable=line-too-long


def generator():
    """
    Top level function that ...
    - reads in the SSDF excel spreadsheet
    - passes data to a jinja2 template
    """
    standard = Standard()

    # Practices are a SSDF specific term for top level requirements
    with open("Secure-Software-Development-Attestation-Form_508c.yml") as file:
        requirements = safe_load(file)

    print(requirements)
    environment = Environment(
        loader=FileSystemLoader("attestation_generator/templates")
    )
    template = environment.get_template("ssaf.cdx.json.template")
    content = template.render(
        serialNumber=uuid4().urn,
        standard=standard,
        requirements=requirements,
        autoescape=True,
    )
    with open("ssaf-DRAFT-2023-11.cdx.json", mode="w", encoding="utf-8") as message:
        message.write(content)


if __name__ == "__main__":  # pragma: no cover
    generator()
