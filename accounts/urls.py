from django.urls import re_path, path
from . import views

app_name = 'accounts'
urlpatterns = [
    re_path(r'^signup/$', views.SignupView.as_view(), name='signup'),
    re_path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        views.activate,
        name='activate'
    ),
    # path(
    #     'activate/<uidb64:uidb64>/<token:token>/',
    #     views.activate,
    #     name='activate',
    # )
]
