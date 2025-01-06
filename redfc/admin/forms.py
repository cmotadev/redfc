from django.contrib.admin.forms import AdminAuthenticationForm
from django_recaptcha import fields
from django_recaptcha import widgets


class AdminAuthenticationWithRecaptchaForm(AdminAuthenticationForm):
    captcha = fields.ReCaptchaField(
        widget=widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )
