from django import forms
from captcha.fields import CaptchaField

from website.models import Contact


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'
