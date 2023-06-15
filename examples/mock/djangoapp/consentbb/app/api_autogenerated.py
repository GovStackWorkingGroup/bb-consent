
# Use the api object from the already-existing api with all
# the views that override these auto-generated views
from .api import api

# Import auto-generated schemas
from . import schemas


@api.post("/config/policy/")
def config_policy_create(request, policy: PolicySchema):
    return { "result": a + b }

@api.get("/config/policy/{policyId}/")
def org_read_policy(request, policyId: str, policyFilter: PolicyFilterSchema):
    return { "result": a + b }

@api.get("/config/policy/{policyId}/revisions/")
def org_list_policy_revisions(request, policyId: str, offset: int, limit: int):
    return { "result": a + b }

@api.put("/config/policy/{id}/")
def org_update_policy(request, id: str, policy: PolicySchema):
    return { "result": a + b }

@api.delete("/config/policy/{id}/")
def org_delete_policy(request, id: str):
    return { "result": a + b }

@api.get("/config/policies/")
def org_list_policy(request, policyFilter: PolicyFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.get("/config/agreement/{agreementId}/")
def config_agreement_read(request, agreementId: str):
    return { "result": a + b }

@api.put("/config/agreement/{agreementId}/")
def org_update_agreement(request, agreementId: str, agreement: AgreementSchema):
    return { "result": a + b }

@api.delete("/config/agreement/{agreementId}/")
def org_delete_agreement(request, agreementId: str):
    return { "result": a + b }

@api.post("/config/agreement/")
def org_create_agreement(request, agreement: AgreementSchema):
    return { "result": a + b }

@api.get("/config/agreements/")
def org_list_agreement(request, agreementFilter: AgreementFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.post("/service/individual/")
def org_individual_create(request, registryReference: RegistryReferenceSchema):
    return { "result": a + b }

@api.get("/service/individual/{individualId}/")
def org_individual_read(request, individualId: str):
    return { "result": a + b }

@api.put("/service/individual/{individualId}/")
def org_individual_update(request, individualId: str):
    return { "result": a + b }

@api.delete("/service/individual/{individualId}/")
def org_individual_delete(request, individualId: str):
    return { "result": a + b }

@api.get("/service/individuals/")
def org_individual_list(request, registryReference: RegistryReferenceSchema, offset: int, limit: int):
    return { "result": a + b }

@api.get("/service/agreement/{agreementId}/")
def service_agreement_read(request, agreementId: str):
    return { "result": a + b }

@api.get("/service/policy/{policyId}/")
def service_policy_read(request, policyId: str):
    return { "result": a + b }

@api.get("/service/purpose/{purposeId}/")
def service_agreement_purpose_read(request, purposeId: str):
    return { "result": a + b }

@api.get("/service/agreement/{agreementId}/agreementdata/")
def service_agreement_data_read(request, agreementId: str):
    return { "result": a + b }

@api.get("/service/verification/agreements/")
def service_verification_agreement_list(request, agreementFilter: AgreementFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.get("/service/verification/agreement/{agreementId}/")
def service_verification_agreement_consent_record_read(request, agreementId: str):
    return { "result": a + b }

@api.get("/service/verification/consentrecords/")
def service_verification_consent_record_list(request, consentRecordFilter: ConsentRecordFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.post("/service/individual/record/agreement/{agreementId}/")
def service_create_individual_consent_record(request, agreementId: str, individualId: str, agreementId: str, revisionId: str):
    return { "result": a + b }

@api.get("/service/individual/record/agreement/{agreementId}/")
def service_read_individual_record_read(request, agreementId: str):
    return { "result": a + b }

@api.post("/service/individual/record/consentrecord/draft/")
def service_create_individual_consent_record_draft(request, individualId: str, agreementId: str, revisionId: str):
    return { "result": a + b }

@api.post("/service/individual/record/consentrecord/")
def service_create_individual_consent_record_and_signature(request, consentRecord: ConsentRecordSchema, signature: SignatureSchema):
    return { "result": a + b }

@api.put("/service/individual/record/consentrecord/{consentRecordId}/")
def service_update_individual_consent_record(request, consentRecordId: str, individual: IndividualSchema, agreement: AgreementSchema, revision: RevisionSchema):
    return { "result": a + b }

@api.post("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_create_individual_consent_record_signature(request, consentRecordId: str):
    return { "result": a + b }

@api.put("/service/individual/record/consentrecord/{consentRecordId}/signature/")
def service_update_individual_consent_record_signature(request, consentRecordId: str, signature: SignatureSchema):
    return { "result": a + b }

@api.get("/service/individual/record/agreement/")
def service_list_individual_record_list(request, offset: int, limit: int):
    return { "result": a + b }

@api.delete("/service/individual/record/")
def service_delete_all_records(request,):
    return { "result": a + b }

@api.get("/audit/trackers/")
def audit_list_trackers(request, offset: int, limit: int):
    return { "result": a + b }

@api.post("/audit/tracker/")
def audit_create_tracker(request, auditTracker: AuditTrackerSchema):
    return { "result": a + b }

@api.get("/audit/tracker/{trackerId}/")
def audit_read_tracker(request, trackerId: str):
    return { "result": a + b }

@api.put("/audit/tracker/{trackerId}/")
def audit_update_tracker(request, trackerId: str, auditTracker: AuditTrackerSchema):
    return { "result": a + b }

@api.delete("/audit/tracker/{trackerId}/")
def audit_delete_tracker(request, trackerId: str):
    return { "result": a + b }

@api.get("/audit/consentrecords/")
def audit_consent_record_list(request, consentRecordFilter: ConsentRecordFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.get("/audit/consentrecord/{consentRecordId}/")
def audit_consent_record_read(request, consentRecordId: str, consentRecord: ConsentRecordSchema):
    return { "result": a + b }

@api.get("/audit/agreements/")
def audit_agreement_list(request, agreementFilter: AgreementFilterSchema, offset: int, limit: int):
    return { "result": a + b }

@api.get("/audit/agreement/{agreementId}/")
def audit_read_record(request, agreementId: str, agreementFilter: AgreementFilterSchema):
    return { "result": a + b }


