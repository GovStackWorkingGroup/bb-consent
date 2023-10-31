
# !!! This code is auto-generated, please do not modify
#
# Use the api object from the already-existing api with all
# the views that override these auto-generated views
from django.shortcuts import get_object_or_404

# Dynamic fixtures
# https://django-dynamic-fixture.readthedocs.io/en/latest/
from ddf import G

from .api import api

# Import auto-generated schemas
from . import schemas

# Import auto-generated models
from . import models

# Please note this little magic detail of django-ninja:
#
# Django Ninja will recognize that the function parameters that match path parameters should be taken from the path,
# and that function parameters that are declared with Schema should be taken from the request body.
# https://django-ninja.dev/guides/input/body/


@api.post("/config/policy/")
def config_create_policy(request, policy: schemas.PolicySchema):
    db_instance = models.Policy.objects.create(**policy.dict())
    return schemas.PolicySchema.from_orm(db_instance).dict()


@api.get("/config/policy/{policyId}/")
def config_read_policy(request, policyId: str, revisionId: str=None):
    db_instance = get_object_or_404(models.Policy, pk=policyId)
    mocked_instance = G(models.Revision)
    object1 = schemas.PolicySchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.put("/config/policy/{policyId}/")
def config_update_policy(request, policyId: str, policy: schemas.PolicySchema):
    return "undefined"


@api.post("/config/policy/{policyId}/")
def config_delete_policy(request, policyId: str):
    db_instance = get_object_or_404(models.Policy, pk=policyId)
    db_instance.delete()
    return {"success": True}


@api.get("/config/policy/{policyId}/revisions/")
def config_list_policy_revisions(request, policyId: str, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Revision, pk=policyId)
    return schemas.RevisionSchema.from_orm(db_instance).dict()


@api.get("/config/policies/")
def config_list_policy(request, revisionId: str=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Policy, pk=revisionId)
    return schemas.PolicySchema.from_orm(db_instance).dict()


@api.get("/config/data-agreement/{dataAgreementId}/")
def config_read_agreement(request, dataAgreementId: str):
    db_instance = get_object_or_404(models.DataAgreement, pk=dataAgreementId)
    mocked_instance = G(models.Revision)
    object1 = schemas.DataAgreementSchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.put("/config/data-agreement/{dataAgreementId}/")
def config_update_agreement(request, dataAgreementId: str, dataAgreement: schemas.DataAgreementSchema):
    return "undefined"


@api.post("/config/data-agreement/{dataAgreementId}/")
def config_delete_agreement(request, dataAgreementId: str):
    db_instance = get_object_or_404(models.DataAgreement, pk=dataAgreementId)
    db_instance.delete()
    return {"success": True}


@api.post("/config/data-agreement/")
def config_create_agreement(request, dataAgreement: schemas.DataAgreementSchema):
    db_instance = models.DataAgreement.objects.create(**dataAgreement.dict())
    return schemas.DataAgreementSchema.from_orm(db_instance).dict()


@api.get("/config/data-agreements/")
def config_list_agreement(request, filterDataAgreementName: str=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.DataAgreement, pk=None)
    return schemas.DataAgreementSchema.from_orm(db_instance).dict()


@api.post("/config/individual/")
def service_individual_create(request, individual: schemas.IndividualSchema):
    db_instance = models.Individual.objects.create(**individual.dict())
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/config/individual/{individualId}/")
def service_individual_read(request, individualId: str):
    db_instance = get_object_or_404(models.Individual, pk=individualId)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/config/individuals/")
def service_individual_list(request, filterFunctionalId: str=None, filterFoundationalId: str=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Individual, pk=filterFunctionalId)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.post("/service/individual/")
def service_individual_create(request, individual: schemas.IndividualSchema):
    db_instance = models.Individual.objects.create(**individual.dict())
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/service/individual/{individualId}/")
def service_individual_read(request, individualId: str):
    db_instance = get_object_or_404(models.Individual, pk=individualId)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.put("/service/individual/{individualId}/")
def service_individual_update(request, individualId: str, individual: schemas.IndividualSchema):
    return "undefined"


@api.get("/service/individuals/")
def service_individual_list(request, filterFunctionalId: str=None, filterFoundationalId: str=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Individual, pk=filterFunctionalId)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/service/data-agreement/{dataAgreementId}/")
def service_agreement_read(request, dataAgreementId: str):
    db_instance = get_object_or_404(models.DataAgreement, pk=dataAgreementId)
    mocked_instance = G(models.Revision)
    object1 = schemas.DataAgreementSchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.get("/service/policy/{policyId}/")
def service_policy_read(request, policyId: str, revisionId: str=None):
    db_instance = get_object_or_404(models.Policy, pk=policyId)
    mocked_instance = G(models.Revision)
    object1 = schemas.PolicySchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.get("/service/data-agreement/{datadataAgreementId}/attributes/")
def service_agreement_data_read(request, datadataAgreementId: str, revisionId: str=None):
    db_instance = get_object_or_404(models.DataAgreementAttribute, pk=datadataAgreementId)
    return schemas.DataAgreementAttributeSchema.from_orm(db_instance).dict()


@api.get("/service/verification/data-agreements/")
def service_verification_agreement_list(request, filterDataAgreementName: str=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/service/verification/consentrecords/")
def service_verification_consent_record_list(request, filterOptIn: str=None, filterDataAgreementId: str=None, filterDataAgreementRevisionId: str=None, filterIndividualId: str=None, filterFunctionalId: str=None, filterFoundationalId: str=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/service/verification/consentrecord/{consentRecordId}")
def service_verification_consent_record_list(request, consentRecordId: str, offset: int=None, limit: int=None):
    return "undefined"


@api.post("/service/individual/record/data-agreement/{dataAgreementId}/")
def service_create_individual_consent_record(request, dataAgreementId: str, individualId: str, revisionId: str=None):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.get("/service/individual/record/data-agreement/{dataAgreementId}/")
def service_read_individual_record_read(request, dataAgreementId: str):
    return "undefined"


@api.post("/service/individual/record/consent-record/draft/")
def service_create_individual_consent_record_draft(request, individualId: str, dataAgreementId: str, revisionId: str=None):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.post("/service/individual/record/consent-record/")
def service_create_individual_consent_record_and_signature(request, ):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.get("/service/individual/record/consent-record/")
def service_list_individual_consent_record_list(request, offset: int=None, limit: int=None):
    return "undefined"


@api.put("/service/individual/record/consent-record/{consentRecordId}/")
def service_update_individual_consent_record(request, consentRecordId: str, consentRecord: schemas.ConsentRecordSchema):
    return "undefined"


@api.post("/service/individual/record/consent-record/{consentRecordId}/signature/")
def service_create_individual_consent_record_signature(request, consentRecordId: str, signature: schemas.SignatureSchema):
    db_instance = models.Signature.objects.create(**signature.dict())
    return schemas.SignatureSchema.from_orm(db_instance).dict()


@api.put("/service/individual/record/consent-record/{consentRecordId}/signature/")
def service_update_individual_consent_record_signature(request, consentRecordId: str, signature: schemas.SignatureSchema):
    return "undefined"


@api.get("/service/individual/record/data-agreement/{dataAgreementId}/all/")
def service_list_individual_agreement_consent_record_list(request, dataAgreementId: str, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.ConsentRecord, pk=dataAgreementId)
    return schemas.ConsentRecordSchema.from_orm(db_instance).dict()


@api.delete("/service/individual/record/")
def service_delete_all_records(request, ):
    return "undefined"


@api.get("/audit/consentrecords/")
def audit_consent_record_list(request, filterOptIn: str=None, filterdataAgreementId: str=None, filterAgreementRevisionId: str=None, filterIndividualId: str=None, filterFunctionalId: str=None, filterFoundationalId: str=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/audit/consentrecord/{consentRecordId}/")
def audit_consent_record_read(request, consentRecordId: str):
    return "undefined"


@api.post("/audit/data-agreements/")
def audit_agreement_list(request, filterDataAgreementName: str=None, offset: int=None, limit: int=None):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.get("/audit/data-agreement/{dataAgreementId}/")
def audit_read_record(request, dataAgreementId: str):
    return "undefined"



