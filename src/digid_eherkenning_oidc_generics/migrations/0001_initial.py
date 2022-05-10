# Generated by Django 3.2.12 on 2022-03-01 13:29

import digid_eherkenning_oidc_generics.models
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields
import mozilla_django_oidc_db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OpenIDConnectEHerkenningConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates whether OpenID Connect for authentication/authorization is enabled",
                        verbose_name="enable",
                    ),
                ),
                (
                    "oidc_rp_client_id",
                    models.CharField(
                        help_text="OpenID Connect client ID provided by the OIDC Provider",
                        max_length=1000,
                        verbose_name="OpenID Connect client ID",
                    ),
                ),
                (
                    "oidc_rp_client_secret",
                    models.CharField(
                        help_text="OpenID Connect secret provided by the OIDC Provider",
                        max_length=1000,
                        verbose_name="OpenID Connect secret",
                    ),
                ),
                (
                    "oidc_rp_sign_algo",
                    models.CharField(
                        default="HS256",
                        help_text="Algorithm the Identity Provider uses to sign ID tokens",
                        max_length=50,
                        verbose_name="OpenID sign algorithm",
                    ),
                ),
                (
                    "oidc_op_discovery_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider discovery endpoint ending with a slash (`.well-known/...` will be added automatically). If this is provided, the remaining endpoints can be omitted, as they will be derived from this endpoint.",
                        max_length=1000,
                        verbose_name="Discovery endpoint",
                    ),
                ),
                (
                    "oidc_op_jwks_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider JSON Web Key Set endpoint. Required if `RS256` is used as signing algorithm",
                        max_length=1000,
                        verbose_name="JSON Web Key Set endpoint",
                    ),
                ),
                (
                    "oidc_op_authorization_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider authorization endpoint",
                        max_length=1000,
                        verbose_name="Authorization endpoint",
                    ),
                ),
                (
                    "oidc_op_token_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider token endpoint",
                        max_length=1000,
                        verbose_name="Token endpoint",
                    ),
                ),
                (
                    "oidc_op_user_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider userinfo endpoint",
                        max_length=1000,
                        verbose_name="User endpoint",
                    ),
                ),
                (
                    "oidc_rp_idp_sign_key",
                    models.CharField(
                        blank=True,
                        help_text="Key the Identity Provider uses to sign ID tokens in the case of an RSA sign algorithm. Should be the signing key in PEM or DER format",
                        max_length=1000,
                        verbose_name="Sign key",
                    ),
                ),
                (
                    "oidc_op_logout_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider logout endpoint",
                        max_length=1000,
                        verbose_name="Logout endpoint",
                    ),
                ),
                (
                    "oidc_keycloak_idp_hint",
                    models.CharField(
                        blank=True,
                        help_text="Specific for Keycloak: parameter that indicates which identity provider should be used (therefore skipping the Keycloak login screen).",
                        max_length=1000,
                        verbose_name="Keycloak Identity Provider hint",
                    ),
                ),
                (
                    "identifier_claim_name",
                    models.CharField(
                        default="kvk",
                        help_text="The name of the claim in which the KVK of the user is stored",
                        max_length=100,
                        verbose_name="KVK claim name",
                    ),
                ),
                (
                    "oidc_rp_scopes_list",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.CharField(
                            max_length=50, verbose_name="OpenID Connect scope"
                        ),
                        blank=True,
                        default=digid_eherkenning_oidc_generics.models.get_default_scopes_kvk,
                        help_text="OpenID Connect scopes that are requested during login. These scopes are hardcoded and must be supported by the identity provider",
                        size=None,
                        verbose_name="OpenID Connect scopes",
                    ),
                ),
            ],
            options={
                "verbose_name": "OpenID Connect configuration for eHerkenning",
            },
            bases=(mozilla_django_oidc_db.models.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name="OpenIDConnectPublicConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates whether OpenID Connect for authentication/authorization is enabled",
                        verbose_name="enable",
                    ),
                ),
                (
                    "oidc_rp_client_id",
                    models.CharField(
                        help_text="OpenID Connect client ID provided by the OIDC Provider",
                        max_length=1000,
                        verbose_name="OpenID Connect client ID",
                    ),
                ),
                (
                    "oidc_rp_client_secret",
                    models.CharField(
                        help_text="OpenID Connect secret provided by the OIDC Provider",
                        max_length=1000,
                        verbose_name="OpenID Connect secret",
                    ),
                ),
                (
                    "oidc_rp_sign_algo",
                    models.CharField(
                        default="HS256",
                        help_text="Algorithm the Identity Provider uses to sign ID tokens",
                        max_length=50,
                        verbose_name="OpenID sign algorithm",
                    ),
                ),
                (
                    "oidc_op_discovery_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider discovery endpoint ending with a slash (`.well-known/...` will be added automatically). If this is provided, the remaining endpoints can be omitted, as they will be derived from this endpoint.",
                        max_length=1000,
                        verbose_name="Discovery endpoint",
                    ),
                ),
                (
                    "oidc_op_jwks_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider JSON Web Key Set endpoint. Required if `RS256` is used as signing algorithm",
                        max_length=1000,
                        verbose_name="JSON Web Key Set endpoint",
                    ),
                ),
                (
                    "oidc_op_authorization_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider authorization endpoint",
                        max_length=1000,
                        verbose_name="Authorization endpoint",
                    ),
                ),
                (
                    "oidc_op_token_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider token endpoint",
                        max_length=1000,
                        verbose_name="Token endpoint",
                    ),
                ),
                (
                    "oidc_op_user_endpoint",
                    models.URLField(
                        help_text="URL of your OpenID Connect provider userinfo endpoint",
                        max_length=1000,
                        verbose_name="User endpoint",
                    ),
                ),
                (
                    "oidc_rp_idp_sign_key",
                    models.CharField(
                        blank=True,
                        help_text="Key the Identity Provider uses to sign ID tokens in the case of an RSA sign algorithm. Should be the signing key in PEM or DER format",
                        max_length=1000,
                        verbose_name="Sign key",
                    ),
                ),
                (
                    "oidc_op_logout_endpoint",
                    models.URLField(
                        blank=True,
                        help_text="URL of your OpenID Connect provider logout endpoint",
                        max_length=1000,
                        verbose_name="Logout endpoint",
                    ),
                ),
                (
                    "oidc_keycloak_idp_hint",
                    models.CharField(
                        blank=True,
                        help_text="Specific for Keycloak: parameter that indicates which identity provider should be used (therefore skipping the Keycloak login screen).",
                        max_length=1000,
                        verbose_name="Keycloak Identity Provider hint",
                    ),
                ),
                (
                    "identifier_claim_name",
                    models.CharField(
                        default="bsn",
                        help_text="The name of the claim in which the BSN of the user is stored",
                        max_length=100,
                        verbose_name="BSN claim name",
                    ),
                ),
                (
                    "oidc_rp_scopes_list",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.CharField(
                            max_length=50, verbose_name="OpenID Connect scope"
                        ),
                        blank=True,
                        default=digid_eherkenning_oidc_generics.models.get_default_scopes_bsn,
                        help_text="OpenID Connect scopes that are requested during login. These scopes are hardcoded and must be supported by the identity provider",
                        size=None,
                        verbose_name="OpenID Connect scopes",
                    ),
                ),
            ],
            options={
                "verbose_name": "OpenID Connect configuration for DigiD",
            },
            bases=(mozilla_django_oidc_db.models.CachingMixin, models.Model),
        ),
    ]