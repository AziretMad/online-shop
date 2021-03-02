from django.urls import re_path, path
from . import views

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
    )
]
