from ninja import ModelSchema, NinjaAPI
from . import models

api = NinjaAPI(urls_namespace="consentbb", version="1.1.0-rc1")


class PolicySchema(ModelSchema):
    class Config:
        model = models.Policy
        model_fields = "__all__"


@api.post("/config/policy/")
def config_policy_create(request, policy: PolicySchema):
    policy = models.Policy.objects.create(**policy.dict())
    return PolicySchema.from_orm(policy)
