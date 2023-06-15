
from ninja import ModelSchema

from . import models


class IndividualSchema(ModelSchema):
    class Config:
        model = models.Individual
        model_fields = "__all__"

class AgreementSchema(ModelSchema):
    class Config:
        model = models.Agreement
        model_fields = "__all__"

class AgreementDataSchema(ModelSchema):
    class Config:
        model = models.AgreementData
        model_fields = "__all__"

class PolicySchema(ModelSchema):
    class Config:
        model = models.Policy
        model_fields = "__all__"

class ConsentRecordSchema(ModelSchema):
    class Config:
        model = models.ConsentRecord
        model_fields = "__all__"

class RevisionSchema(ModelSchema):
    class Config:
        model = models.Revision
        model_fields = "__all__"

class AgreementFilterSchema(ModelSchema):
    class Config:
        model = models.AgreementFilter
        model_fields = "__all__"

class ConsentRecordFilterSchema(ModelSchema):
    class Config:
        model = models.ConsentRecordFilter
        model_fields = "__all__"

class PolicyFilterSchema(ModelSchema):
    class Config:
        model = models.PolicyFilter
        model_fields = "__all__"

class ControllerSchema(ModelSchema):
    class Config:
        model = models.Controller
        model_fields = "__all__"

class SignatureSchema(ModelSchema):
    class Config:
        model = models.Signature
        model_fields = "__all__"

class AgreementPurposeSchema(ModelSchema):
    class Config:
        model = models.AgreementPurpose
        model_fields = "__all__"

class AgreementLifecycleSchema(ModelSchema):
    class Config:
        model = models.AgreementLifecycle
        model_fields = "__all__"

class RegistryReferenceSchema(ModelSchema):
    class Config:
        model = models.RegistryReference
        model_fields = "__all__"

class AuditTrackerSchema(ModelSchema):
    class Config:
        model = models.AuditTracker
        model_fields = "__all__"

class AuditEventTypeSchema(ModelSchema):
    class Config:
        model = models.AuditEventType
        model_fields = "__all__"

class StatusStartupSchema(ModelSchema):
    class Config:
        model = models.StatusStartup
        model_fields = "__all__"

class StatusReadinessSchema(ModelSchema):
    class Config:
        model = models.StatusReadiness
        model_fields = "__all__"


