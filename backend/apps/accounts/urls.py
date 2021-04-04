from django.urls import re_path, path

from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        views.activate,
        name="activate",
    ),
    path("signin/", views.SignInView.as_view(), name="sign_in"),
    path(
        "activation-info/", views.ActivationInfoView.as_view(),
        name="activation_info"
    ),
    path(
        "activation-done/", views.ActivationDoneView.as_view(),
        name="activation_done"
    ),
    path(
        "logout/",
        views._logout,
        name="logout",
    ),
    path(
        "password-reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    re_path(
        r"^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "update-account/<int:pk>/",
        views.UpdateAccountView.as_view(),
        name="update_account",
    ),
    path("api/create/", views.CreateUserAPIView.as_view()),
]
