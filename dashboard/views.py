from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def dashboard_view(request):
    # Verificar si el usuario está autenticado a través de Firebase
    if "user" not in request.session:
        return redirect("login:login")

    user_info = request.session.get("user", {})
    return render(request, "dashboard/dashboard.html", {"user": user_info})
