from django.contrib import admin, messages
from django.contrib.admin.actions import delete_selected as _delete_selected
from django.urls import reverse
from django.utils.html import escape, format_html
from django.utils.translation import ugettext_lazy as _

from ..forms import FormDefinitionForm
from ..models import Form, FormDefinition


def delete_selected(modeladmin, request, queryset):
    actively_used = queryset.filter(formstep__isnull=False)
    for name in actively_used.values_list("name", flat=True):
        messages.error(
            request,
            _(
                "{name} kan niet verwijderd worden omdat deze in één of meerdere formulieren gebruikt wordt."
            ).format(name=name),
        )
    safe_to_delete = queryset.exclude(id__in=actively_used.values_list("id", flat=True))
    return _delete_selected(modeladmin, request, safe_to_delete)


delete_selected.allowed_permissions = ("delete",)
delete_selected.short_description = _("Delete selected %(verbose_name_plural)s")


@admin.register(FormDefinition)
class FormDefinitionAdmin(admin.ModelAdmin):
    form = FormDefinitionForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "used_in_forms")
    actions = ["overridden_delete_selected", "make_copies"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        (old_func, name, short_description) = actions["delete_selected"]
        actions["delete_selected"] = (delete_selected, name, short_description)
        return actions

    def make_copies(self, request, queryset):
        for instance in queryset:
            instance.copy()

    make_copies.short_description = _("Kopieer geselecteerde %(verbose_name_plural)s.")

    def used_in_forms(self, obj) -> str:
        forms = Form.objects.filter(formstep__form_definition=obj)
        html = "<ul>"
        for form in forms:
            form_url = reverse(
                "admin:forms_form_change",
                kwargs={"object_id": form.pk},
            )
            html += f"<li><a href={form_url}>{escape(form.name)}</a></li>"
        html += "</ul>"
        return format_html(html)

    used_in_forms.short_description = _("In gebruik in:")
