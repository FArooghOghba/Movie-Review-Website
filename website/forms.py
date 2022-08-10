from django.forms import ModelForm
from captcha.fields import CaptchaField

from website.models import Contact, Newsletter


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
