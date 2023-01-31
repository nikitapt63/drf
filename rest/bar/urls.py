from django.urls import path
from .endpoints import PageListView


urlpatterns = [
    path("pages/", PageListView.as_view())
]
