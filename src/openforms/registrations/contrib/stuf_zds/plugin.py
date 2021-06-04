from pprint import pprint
from typing import Optional

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from openforms.registrations.contrib.stuf_zds.models import StufZDSConfig
from openforms.registrations.registry import register
from openforms.submissions.models import Submission


class ZaakOptionsSerializer(serializers.Serializer):
    zds_zaaktype_code = serializers.CharField(
        required=False,
        help_text=_("Zaaktype code for newly created Zaken in StUF-ZDS"),
    )
    zds_zaaktype_omschrijving = serializers.CharField(
        required=False,
        help_text=_("Zaaktype description for newly created Zaken in StUF-ZDS"),
    )


@register(
    "stuf-zds-create-zaak",
    _("StUF-ZDS"),
    configuration_options=ZaakOptionsSerializer,
)
def create_zaak_plugin(submission: Submission, options: dict) -> Optional[dict]:
    data = submission.get_merged_data()

    config = StufZDSConfig.get_solo()
    config.apply_defaults_to(options)

    options["omschrijving"] = submission.form.name
    options["referentienummer"] = str(submission.uuid)

    # "bsn"
    # "nnp_id"
    # "vestigings_nummer"
    # "anp_id"

    client = config.get_client(options)

    zaak_id = client.create_zaak_identificatie()
    client.create_zaak(zaak_id, data)

    doc_id = client.create_document_identificatie()
    client.create_zaak_document(zaak_id, doc_id, data)

    result = {
        "zaak": zaak_id,
        "document": doc_id,
    }
    return result