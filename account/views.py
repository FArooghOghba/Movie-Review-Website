from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomAuthenticationForm


def logout_view(request):
    logout(request)
    return redirect('/')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'account/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('website:home_page'))
