from django.test import override_settings
from django.urls import reverse

from django_webtest import WebTest

from openforms.accounts.tests.factories import SuperUserFactory


@override_settings(TWO_FACTOR_PATCH_ADMIN=False)
class FormVersionAdminImportExportTests(WebTest):
    def setUp(self):
        self.user = SuperUserFactory.create()

    def test_form(self):
        response = self.app.get(
            reverse("admin:forms_formversion_add"), user=self.user, status=403
        )

        self.assertEqual(403, response.status_code)