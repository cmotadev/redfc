from django.contrib.admin.apps import AdminConfig


class RedFCAdminConfig(AdminConfig):
    default_site = "redfc.admin.RedFCAdminSite"
