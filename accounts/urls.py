from django.urls import re_path, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from . forms import CustomPasswordResetForm

app_name = 'accounts'
urlpatterns = [
    path(
        'signup/',
        views.SignupView.as_view(),
        name='signup'
    ),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        views.activate,
        name='activate'
    ),
    path(
        'signin/',
        views.SignInView.as_view(),
        name='sign_in'
    ),
    path(
        'activation-info/',
        views.ActivationInfoView.as_view(),
        name="activation_info"
    ),
    path(
        'activation-done/',
        views.ActivationDoneView.as_view(),
        name='activation_done'
    ),
    path(
        'invalid-link/',
        views.InvalidLinkView.as_view(),
        name='invalid_link'
    ),
    path(
        'logout/',
        views._logout,
        name='logout',
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('accounts:password_reset_done'),
            form_class=CustomPasswordResetForm
        ),
        name='password_reset'
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    re_path(
        r"^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
