from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # Paths for forgetting passwords and resetting the user password.
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='account/reset_password.html',
             email_template_name='account/password_reset_email.html',
             success_url=reverse_lazy('account:password_reset_done')),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/reset_password_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/reset_password_confirm.html',
             success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/reset_password_complete.html'),
         name='password_reset_complete'),

]
