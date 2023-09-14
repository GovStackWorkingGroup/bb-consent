import json
import pgpy

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from hashlib import sha1

from django.core import serializers


from . import models


pgp_example_private = """
-----BEGIN PGP PRIVATE KEY BLOCK-----

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
jj45+U3gbHkSkBwO8tw=
=hlZf
-----END PGP PRIVATE KEY BLOCK-----
""".lstrip()


def json_serialize(instance, **revision_fields):
    # Convert the instance data to sorted, indented JSON

    if instance:
        response = serializers.serialize('json', [instance, ], indent=2)

        # Strip the list
        json_dict = json.loads(response)
        revision_fields["object_data"] = json_dict[0]["fields"]

    response = json.dumps(revision_fields, indent=2)

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

    if instance:
        json_revision_data = json_serialize(
            instance,
            schema_name=schema_name,
            object_id=object_id,
            timestamp=timestamp,
            authorized_by_other=authorized_by_other,
            authorized_by_individual=authorized_by_individual,
        )
    else:
        json_revision_data = ""
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

    return new_revision


def create_signature_for_revision(revision):
    signature = models.Signature()

    private_key = pgpy.PGPKey()
    private_key.parse(pgp_example_private)

    signature.verification_method = "pgp"
    signature.timestamp = timezone.now()
    signature.verification_artifact = ""
    signature.verification_signed_by = private_key.fingerprint  # PGP fingerprint
    signature.verification_signed_as = "individual"
    signature.object_type = "Revision"
    signature.object_reference = revision.pk

    signature.verification_payload = revision.serialized_snapshot
    signature.verification_payload_hash = revision.serialized_hash

    signature.payload = json_serialize(
        {},
        verification_method=signature.verification_method,
        timestamp=str(signature.timestamp),
        verification_artifact=signature.verification_artifact,
        verification_signed_by=signature.verification_signed_by,
        verification_signed_as=signature.verification_signed_as,
        object_type=signature.object_type,
        object_reference=signature.object_reference,
    )

    signature.signature = private_key.sign(signature.payload)

    signature.save()


@receiver(post_save, sender=models.Agreement)
def revision_agreements(sender, **kwargs):
    revision_any_instance(authorized_by_other="Configuration admin user 'admin'", **kwargs)


@receiver(post_save, sender=models.Policy)
def revision_policy(sender, **kwargs):
    revision_any_instance(authorized_by_other="Configuration admin user 'admin'", **kwargs)


@receiver(post_save, sender=models.ConsentRecord)
def revision_consent_record(sender, **kwargs):
    instance = kwargs.get("instance")
    revision = revision_any_instance(authorized_by_individual=instance.individual.pk, **kwargs)

    create_signature_for_revision(revision)
