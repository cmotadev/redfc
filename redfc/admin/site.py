from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import AdminAuthenticationWithRecaptchaForm


class RedFCAdminSite(admin.AdminSite):
    site_header = _("RED FC administration")
    site_title = _("RED FC site admin")
    login_form = AdminAuthenticationWithRecaptchaForm

    def get_urls(self):
        reset_password_patterns = [
            path(
                "admin/password_reset/",
                auth_views.PasswordResetView.as_view(
                    success_url=reverse_lazy("admin:password_reset_done")
                ),
                name="password_reset",
            ),
            path(
                "admin/password_reset/done/",
                auth_views.PasswordResetDoneView.as_view(),
                name="password_reset_done",
            ),
            path(
                "reset/<uidb64>/<token>/",
                auth_views.PasswordResetConfirmView.as_view(
                    success_url=reverse_lazy("admin:password_reset_complete")
                ),
                name="password_reset_confirm",
            ),
            path(
                "reset/done/",
                auth_views.PasswordResetCompleteView.as_view(),
                name="password_reset_complete",
            )
        ]

        return reset_password_patterns + super().get_urls()