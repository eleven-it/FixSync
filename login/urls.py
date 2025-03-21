from django.urls import path
from .views import login_view, index, signup_view

app_name = "login"  # Definir el namespace para la app

urlpatterns = [
    path("", index, name="inicio"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
]