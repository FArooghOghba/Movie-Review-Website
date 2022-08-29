from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def logout_view(request):
    logout(request)
    return redirect('/')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_message = 'account: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('website:home_page')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'account/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('website:home_page'))
