
# !!! This code is auto-generated, please do not modify

from ninja import ModelSchema
from ninja import Schema

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

class AgreementFilterSchema(Schema):

    name: str


class ConsentRecordFilterSchema(Schema):

    opt_in: bool

    agreement: int

    agreement_revision: int

    individual: int

    functional_id: str

    foundational_id: str


class PolicyFilterSchema(Schema):

    name: str

    revision: int


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

class StatusStartupSchema(Schema):

    status: str

    error_message: str

    waiting_for: str


class StatusReadinessSchema(Schema):

    status: str

    error_message: str

    waiting_for: str



