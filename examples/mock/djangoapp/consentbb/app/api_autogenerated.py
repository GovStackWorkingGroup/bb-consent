
# Use the api object from the already-existing api with all
# the views that override these auto-generated views
from .api import api

# Import auto-generated schemas
from . import schemas

# Import auto-generated models
from . import models


@api.post("/config/policy/")
def config_policy_create(request, policy: schemas.PolicySchema):
    db_instance = models.Policy.objects.create(**policy.dict())
    return schemas.PolicySchema.from_orm(db_instance)


@api.get("/config/policy/{policyId}/")
def org_read_policy(request, policyId: str, policyFilter: schemas.PolicyFilterSchema):
    return "undefined"


@api.get("/config/policy/{policyId}/revisions/")
def org_list_policy_revisions(request, policyId: str, offset: int, limit: int):
    return "undefined"


@api.put("/config/policy/{id}/")
def org_update_policy(request, id: str, policy: schemas.PolicySchema):
    return "undefined"


@api.delete("/config/policy/{id}/")
def org_delete_policy(request, id: str):
    return "undefined"


@api.get("/config/policies/")
def org_list_policy(request, policyFilter: schemas.PolicyFilterSchema, offset: int, limit: int):
    return "undefined"


@api.get("/config/agreement/{agreementId}/")
def config_agreement_read(request, agreementId: str):
    return "undefined"


@api.put("/config/agreement/{agreementId}/")
def org_update_agreement(request, agreementId: str, agreement: schemas.AgreementSchema):
    return "undefined"


@api.delete("/config/agreement/{agreementId}/")
def org_delete_agreement(request, agreementId: str):
    return "undefined"


@api.post("/config/agreement/")
def org_create_agreement(request, agreement: schemas.AgreementSchema):
    db_instance = models.Agreement.objects.create(**agreement.dict())
    return schemas.AgreementSchema.from_orm(db_instance)


@api.get("/config/agreements/")
def org_list_agreement(request, agreementFilter: schemas.AgreementFilterSchema, offset: int, limit: int):
    return "undefined"


@api.post("/service/individual/")
def org_individual_create(request, registryReference: schemas.RegistryReferenceSchema):
    db_instance = models.RegistryReference.objects.create(**registryReference.dict())
    return schemas.RegistryReferenceSchema.from_orm(db_instance)


@api.get("/service/individual/{individualId}/")
def org_individual_read(request, individualId: str):
    return "undefined"


@api.put("/service/individual/{individualId}/")
def org_individual_update(request, individualId: str):
    return "undefined"


@api.delete("/service/individual/{individualId}/")
def org_individual_delete(request, individualId: str):
    return "undefined"


@api.get("/service/individuals/")
def org_individual_list(request, registryReference: schemas.RegistryReferenceSchema, offset: int, limit: int):
    return "undefined"


@api.get("/service/agreement/{agreementId}/")
def service_agreement_read(request, agreementId: str):
    return "undefined"


@api.get("/service/policy/{policyId}/")
def service_policy_read(request, policyId: str):
    return "undefined"


@api.get("/service/purpose/{purposeId}/")
def service_agreement_purpose_read(request, purposeId: str):
    return "undefined"


@api.get("/service/agreement/{agreementId}/agreementdata/")
def service_agreement_data_read(request, agreementId: str):
    return "undefined"


@api.get("/service/verification/agreements/")
def service_verification_agreement_list(request, agreementFilter: schemas.AgreementFilterSchema, offset: int, limit: int):
    return "undefined"


@api.get("/service/verification/agreement/{agreementId}/")
def service_verification_agreement_consent_record_read(request, agreementId: str):
    return "undefined"


@api.get("/service/verification/consentrecords/")
def service_verification_consent_record_list(request, consentRecordFilter: schemas.ConsentRecordFilterSchema, offset: int, limit: int):
    return "undefined"


@api.post("/service/individual/record/agreement/{agreementId}/")
def service_create_individual_consent_record(request, agreementId: str, individualId: str, revisionId: str):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance)


@api.get("/service/individual/record/agreement/{agreementId}/")
def service_read_individual_record_read(request, agreementId: str):
    return "undefined"


@api.post("/service/individual/record/consentrecord/draft/")
def service_create_individual_consent_record_draft(request, individualId: str, agreementId: str, revisionId: str):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance)


@api.post("/service/individual/record/consentrecord/")
def service_create_individual_consent_record_and_signature(request, consentRecord: schemas.ConsentRecordSchema, signature: schemas.SignatureSchema):
    db_instance = models.ConsentRecord.objects.create(**consentRecord.dict())
    return schemas.ConsentRecordSchema.from_orm(db_instance)


@api.put("/service/individual/record/consentrecord/{consentRecordId}/")
def service_update_individual_consent_record(request, consentRecordId: str, individual: schemas.IndividualSchema, agreement: schemas.AgreementSchema, revision: schemas.RevisionSchema):
    return "undefined"


@api.post("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_create_individual_consent_record_signature(request, consentRecordId: str):
    db_instance = models.TBD.objects.create()
    return schemas.TBDSchema.from_orm(db_instance)


@api.put("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_update_individual_consent_record_signature(request, consentRecordId: str, signature: schemas.SignatureSchema):
    return "undefined"


@api.get("/service/individual/record/agreement/")
def service_list_individual_record_list(request, offset: int, limit: int):
    return "undefined"


@api.delete("/service/individual/record/")
def service_delete_all_records(request,):
    return "undefined"


@api.get("/audit/trackers/")
def audit_list_trackers(request, offset: int, limit: int):
    return "undefined"


@api.post("/audit/tracker/")
def audit_create_tracker(request, auditTracker: schemas.AuditTrackerSchema):
    db_instance = models.AuditTracker.objects.create(**auditTracker.dict())
    return schemas.AuditTrackerSchema.from_orm(db_instance)


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
def audit_consent_record_list(request, consentRecordFilter: schemas.ConsentRecordFilterSchema, offset: int, limit: int):
    return "undefined"


@api.get("/audit/consentrecord/{consentRecordId}/")
def audit_consent_record_read(request, consentRecordId: str, consentRecord: schemas.ConsentRecordSchema):
    return "undefined"


@api.get("/audit/agreements/")
def audit_agreement_list(request, agreementFilter: schemas.AgreementFilterSchema, offset: int, limit: int):
    return "undefined"


@api.get("/audit/agreement/{agreementId}/")
def audit_read_record(request, agreementId: str, agreementFilter: schemas.AgreementFilterSchema):
    return "undefined"


@api.get("/status/startup/")
def status_startup(request,):
    return "undefined"


@api.get("/status/readiness/")
def status_readiness(request,):
    return "undefined"



