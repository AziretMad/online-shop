from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path("", views.ItemList.as_view(), name="index")
]
