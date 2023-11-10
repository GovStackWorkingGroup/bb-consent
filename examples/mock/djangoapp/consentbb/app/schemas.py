
# !!! This code is auto-generated, please do not modify

from ninja import ModelSchema
from ninja import Schema

from . import models


class IndividualSchema(ModelSchema):
    class Config:
        model = models.Individual
        model_fields = "__all__"

class DataAgreementSchema(ModelSchema):
    class Config:
        model = models.DataAgreement
        model_fields = "__all__"

class DataAgreementAttributeSchema(ModelSchema):
    class Config:
        model = models.DataAgreementAttribute
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

class DataAgreementLifecycleSchema(ModelSchema):
    class Config:
        model = models.DataAgreementLifecycle
        model_fields = "__all__"

class WebhookSchema(ModelSchema):
    class Config:
        model = models.Webhook
        model_fields = "__all__"

class WebhookEventSchema(ModelSchema):
    class Config:
        model = models.WebhookEvent
        model_fields = "__all__"

class WebhookEventSubscriptionSchema(ModelSchema):
    class Config:
        model = models.WebhookEventSubscription
        model_fields = "__all__"


