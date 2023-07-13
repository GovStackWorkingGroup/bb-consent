from django.core.management.base import BaseCommand, CommandError


from ... import models


class Command(BaseCommand):
    help = "Creates example fixtures from OpenAPI spec"

    def handle(self, *args, **options):
        # Example policy
        policy, __ = models.Policy.objects.get_or_create(
            name="test policy",
            version="0.1",
            url="https://example-consent.com/policy/test-policy/v0.1/"
        )
