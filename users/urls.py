"""Defines URL patterns for users."""

from django.contrib.auth.views import LoginView
from django.urls import path, re_path

from . import views

app_name = "users"
urlpatterns = [
    # Login page
    re_path(
        r"^login/$", LoginView.as_view(template_name="users/login.j2"), name="login"
    ),
    # Logout page
    re_path(r"^logout/$", views.logout_view, name="logout"),

    # Registration page
    re_path(r"^register/$", views.register, name="register"),
]
