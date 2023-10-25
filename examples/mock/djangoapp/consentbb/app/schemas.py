
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

class ControllerSchema(ModelSchema):
    class Config:
        model = models.Controller
        model_fields = "__all__"

class SignatureSchema(ModelSchema):
    class Config:
        model = models.Signature
        model_fields = "__all__"

class AgreementLifecycleSchema(ModelSchema):
    class Config:
        model = models.AgreementLifecycle
        model_fields = "__all__"


