from django.urls import path
from . import views

app_name = "tasks"  # This line sets up the namespace

urlpatterns = [
  path("", views.index, name="index"),
  path("add/", views.add, name="add"),
]