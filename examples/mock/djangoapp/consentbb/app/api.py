from ninja import ModelSchema, NinjaAPI
from . import models

api = NinjaAPI(urls_namespace="consentbb", version="1.1.0-rc1")


# If we were going to overwrite an endpoint, we could do it like this:
# @api.post("/config/policy/")
# def config_policy_create(request, policy: PolicySchema):
#     policy = models.Policy.objects.create(**policy.dict())
#     return PolicySchema.from_orm(policy)
