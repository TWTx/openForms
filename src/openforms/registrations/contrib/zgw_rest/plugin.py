from typing import Optional

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from openforms.registrations.contrib.zgw_rest.models import ZgwConfig
from openforms.registrations.contrib.zgw_rest.service import (
    create_document,
    create_zaak,
    relate_document,
)
from openforms.registrations.registry import register
from openforms.submissions.models import Submission


class ZaakOptionsSerializer(serializers.Serializer):
    zaaktype = serializers.URLField(help_text=_("URL of the ZAAKTYPE in Catalogi API"))
    informatieobjecttype = serializers.URLField(
        help_text=_("URL of the INFORMATIEOBJECTTYPE in Catalogi API")
    )
    organisatie_rsin = serializers.CharField(
        help_text=_("RSIN of organization, which creates the ZAAK")
    )


@register(
    "zgw-create-zaak",
    "Create ZGW Zaak",
    configuration_options=ZaakOptionsSerializer,
    # backend_feedback_serializer=BackendFeedbackSerializer,
)
def create_zaak_plugin(submission: Submission, options: dict) -> Optional[dict]:
    data = {}
    for step in submission.steps:
        data.update(step.data)

    zgw = ZgwConfig.get_solo()
    zgw.apply_defaults_to(options)

    zaak = create_zaak(options)
    document = create_document(name=submission.form.name, body=data, options=options)
    relate_document(zaak["url"], document["url"])

    result = {
        "zaak": zaak,
        "document": document,
    }
    return result
