
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


@api.post("/config/policy/")
def config_create_policy(request, policy: schemas.PolicySchema):
    db_instance = models.Policy.objects.create(**policy.dict())
    return schemas.PolicySchema.from_orm(db_instance).dict()


@api.get("/config/policy/{policyId}/")
def config_read_policy(request, policyId: str, policyFilter: schemas.PolicyFilterSchema=None):
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
def config_list_policy(request, policyFilter: schemas.PolicyFilterSchema=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Policy, pk=None)
    return schemas.PolicySchema.from_orm(db_instance).dict()


@api.get("/config/agreement/{agreementId}/")
def config_read_agreement(request, agreementId: str):
    db_instance = get_object_or_404(models.Agreement, pk=agreementId)
    mocked_instance = G(models.Revision)
    object1 = schemas.AgreementSchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.put("/config/agreement/{agreementId}/")
def config_update_agreement(request, agreementId: str, agreement: schemas.AgreementSchema):
    return "undefined"


@api.post("/config/agreement/{agreementId}/")
def config_delete_agreement(request, agreementId: str):
    db_instance = get_object_or_404(models.Agreement, pk=agreementId)
    db_instance.delete()
    return {"success": True}


@api.post("/config/agreement/")
def config_create_agreement(request, agreement: schemas.AgreementSchema):
    db_instance = models.Agreement.objects.create(**agreement.dict())
    return schemas.AgreementSchema.from_orm(db_instance).dict()


@api.get("/config/agreements/")
def config_list_agreement(request, agreementFilter: schemas.AgreementFilterSchema=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Agreement, pk=None)
    return schemas.AgreementSchema.from_orm(db_instance).dict()


@api.post("/service/individual/")
def service_individual_create(request, registryReference: schemas.RegistryReferenceSchema=None):
    db_instance = models.Individual.objects.create(**registryReference.dict())
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/service/individual/{individualId}/")
def service_individual_read(request, individualId: str):
    db_instance = get_object_or_404(models.Individual, pk=individualId)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.put("/service/individual/{individualId}/")
def service_individual_update(request, individualId: str):
    return "undefined"


@api.post("/service/individual/{individualId}/")
def service_individual_delete(request, individualId: str):
    db_instance = get_object_or_404(models.Individual, pk=individualId)
    db_instance.delete()
    return {"success": True}


@api.get("/service/individuals/")
def service_individual_list(request, registryReference: schemas.RegistryReferenceSchema=None, offset: int=None, limit: int=None):
    db_instance = get_object_or_404(models.Individual, pk=None)
    return schemas.IndividualSchema.from_orm(db_instance).dict()


@api.get("/service/agreement/{agreementId}/")
def service_agreement_read(request, agreementId: str):
    db_instance = get_object_or_404(models.Agreement, pk=agreementId)
    mocked_instance = G(models.Revision)
    object1 = schemas.AgreementSchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.get("/service/policy/{policyId}/")
def service_policy_read(request, policyId: str):
    db_instance = get_object_or_404(models.Policy, pk=policyId)
    mocked_instance = G(models.Revision)
    object1 = schemas.PolicySchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.get("/service/purpose/{purposeId}/")
def service_agreement_purpose_read(request, purposeId: str):
    db_instance = get_object_or_404(models.AgreementPurpose, pk=purposeId)
    mocked_instance = G(models.Revision)
    object1 = schemas.AgreementPurposeSchema.from_orm(db_instance).dict()
    object2 = schemas.RevisionSchema.from_orm(mocked_instance).dict()
    return [object1, object2]


@api.get("/service/agreement/{agreementId}/agreementdata/")
def service_agreement_data_read(request, agreementId: str):
    db_instance = get_object_or_404(models.AgreementData, pk=agreementId)
    return schemas.AgreementDataSchema.from_orm(db_instance).dict()


@api.get("/service/verification/agreements/")
def service_verification_agreement_list(request, agreementFilter: schemas.AgreementFilterSchema=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/service/verification/agreement/{agreementId}/")
def service_verification_agreement_consent_record_read(request, agreementId: str):
    return "undefined"


@api.get("/service/verification/consentrecords/")
def service_verification_consent_record_list(request, consentRecordFilter: schemas.ConsentRecordFilterSchema=None, offset: int=None, limit: int=None):
    return "undefined"


@api.post("/service/individual/record/agreement/{agreementId}/")
def service_create_individual_consent_record(request, agreementId: str, individualId: str, revisionId: str=None):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.get("/service/individual/record/agreement/{agreementId}/")
def service_read_individual_record_read(request, agreementId: str):
    return "undefined"


@api.post("/service/individual/record/consentrecord/draft/")
def service_create_individual_consent_record_draft(request, individualId: str, agreementId: str, revisionId: str=None):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.post("/service/individual/record/consentrecord/")
def service_create_individual_consent_record_and_signature(request, consentRecord: schemas.ConsentRecordSchema, signature: schemas.SignatureSchema):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.put("/service/individual/record/consentrecord/{consentRecordId}/")
def service_update_individual_consent_record(request, consentRecordId: str, individualId: str, agreementId: str, revisionId: str=None):
    return "undefined"


@api.post("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_create_individual_consent_record_signature(request, consentRecordId: str):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.put("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_update_individual_consent_record_signature(request, consentRecordId: str, signature: schemas.SignatureSchema):
    return "undefined"


@api.get("/service/individual/record/agreement/{agreementId}/all/")
def service_list_individual_record_list(request, agreementId: str, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/service/individual/record/")
def service_list_individual_record_list(request, offset: int=None, limit: int=None):
    return "undefined"


@api.delete("/service/individual/record/")
def service_delete_all_records(request,):
    return "undefined"


@api.get("/audit/trackers/")
def audit_list_trackers(request, offset: int=None, limit: int=None):
    return "undefined"


@api.post("/audit/tracker/")
def audit_create_tracker(request, auditTracker: schemas.AuditTrackerSchema):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance).dict()


@api.get("/audit/tracker/{trackerId}/")
def audit_read_tracker(request, trackerId: str):
    return "undefined"


@api.put("/audit/tracker/{trackerId}/")
def audit_update_tracker(request, trackerId: str, auditTracker: schemas.AuditTrackerSchema):
    return "undefined"


@api.delete("/audit/tracker/{trackerId}/")
def audit_delete_tracker(request, trackerId: str):
    return "undefined"


@api.get("/audit/consentrecords/")
def audit_consent_record_list(request, consentRecordFilter: schemas.ConsentRecordFilterSchema=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/audit/consentrecord/{consentRecordId}/")
def audit_consent_record_read(request, consentRecordId: str):
    return "undefined"


@api.get("/audit/agreements/")
def audit_agreement_list(request, agreementFilter: schemas.AgreementFilterSchema=None, offset: int=None, limit: int=None):
    return "undefined"


@api.get("/audit/agreement/{agreementId}/")
def audit_read_record(request, agreementId: str, agreementFilter: schemas.AgreementFilterSchema=None):
    return "undefined"


@api.get("/status/startup/")
def status_startup(request,):
    return "undefined"


@api.get("/status/readiness/")
def status_readiness(request,):
    return "undefined"



