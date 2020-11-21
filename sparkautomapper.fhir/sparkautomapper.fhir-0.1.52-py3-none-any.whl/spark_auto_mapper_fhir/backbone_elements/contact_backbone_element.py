from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.valuesets.contactentity_type import ContactEntityTypeCode


class ContactBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        purpose: Optional[CodeableConcept[ContactEntityTypeCode]] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None
    ) -> None:
        """
        ContactBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.contact
        Contact for the product


        :param purpose: The type of contact
        :param name: A name associated with the contact
        :param telecom: Contact details (telephone, email, etc.) for a contact
        :param address: Visiting or postal addresses for the contact
        """
        super().__init__(
            purpose=purpose, name=name, telecom=telecom, address=address
        )
