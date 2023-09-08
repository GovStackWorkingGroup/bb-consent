import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from hashlib import sha1

from django.core import serializers


from . import models


def json_serialize(instance, **revision_fields):
    # Convert the instance data to sorted, indented JSON
    response = serializers.serialize('json', [instance, ], indent=2)

    # Strip the list
    json_dict = json.loads(response)

    # Write the final dictionary that we will serialize
    revisioned_data = {
        "object_data": json_dict[0]["fields"],
        **revision_fields
    }

    response = json.dumps(revisioned_data, indent=2)

    return response


def sha1_hash(data):
    hash_value = sha1(data.encode())
    return hash_value.hexdigest()


def revision_any_instance(**kwargs):

    created = kwargs.get("created", False)
    instance = kwargs.get("instance")

    schema_name = instance._meta.model.__name__
    object_id = instance.pk
    timestamp = str(timezone.now())
    authorized_by_other = kwargs.get("authorized_by_other", None)
    authorized_by_individual = kwargs.get("authorized_by_individual", None)

    predecessor_hash = None

    json_revision_data = json_serialize(
        instance,
        schema_name=schema_name,
        object_id=object_id,
        timestamp=timestamp,
        authorized_by_other=authorized_by_other,
        authorized_by_individual=authorized_by_individual,
    )
    serialized_hash = sha1_hash(json_revision_data)

    if not created:
        predecessor = models.Revision.objects.get(
            schema_name=schema_name,
            object_id=object_id,
            successor=None
        )
        predecessor_hash = predecessor.serialized_hash

    new_revision = models.Revision.objects.create(
        serialized_snapshot=json_revision_data,
        serialized_hash=serialized_hash,
        schema_name=schema_name,
        object_id=object_id,
        timestamp=timestamp,
        authorized_by_other=authorized_by_other,
        predecessor_hash=predecessor_hash
    )

    if not created:
        predecessor.successor = new_revision
        predecessor.save()


@receiver(post_save, sender=models.Agreement)
def revision_agreements(sender, **kwargs):
    revision_any_instance(authorized_by_other="Configuration admin user Jane", **kwargs)


#@receiver(post_save, sender=models.Agreement)
#def revision_policy(sender, **kwargs):
#    revision_any_instance(authorized_by_other="Configuration admin user Jane", **kwargs)
