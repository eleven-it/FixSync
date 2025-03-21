from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")  # Página de inicio

def signup_view(request):
    return render(request, "signup.html")