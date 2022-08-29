from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class CustomUserCreationForm(PopRequestMixin,
                             CreateUpdateAjaxMixin,
                             UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email


class CustomAuthenticationForm(AuthenticationForm):

    def clean_username(self):
        username = self.data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except ObjectDoesNotExist:
                raise ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
        return username

    class Meta:
        model = User
        fields = ['username', 'password']
