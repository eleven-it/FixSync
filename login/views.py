
import json
import firebase_admin.auth as auth

from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_admin import auth
from django.views.decorators.csrf import csrf_exempt

def firebase_config_js(request):
    config = settings.FIREBASE_CONFIG

    login_url = reverse("login:login")
    logout_url = reverse("login:logout")
    reset_url = reverse("login:reset_password")

    js_content = f"""
// Archivo generado automáticamente por Django

const firebaseConfig = {{
    apiKey: "{config['apiKey']}",
    authDomain: "{config['authDomain']}",
    projectId: "{config['projectId']}",
    storageBucket: "{config['storageBucket']}",
    messagingSenderId: "{config['messagingSenderId']}",
    appId: "{config['appId']}",
    measurementId: "{config['measurementId']}"
}};

const backendRoutes = {{
    login: "{login_url}",
    logout: "{logout_url}",
    resetPassword: "{reset_url}"
}};

export {{ firebaseConfig, backendRoutes }};
"""

    return HttpResponse(js_content, content_type="application/javascript")




@csrf_exempt  
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id_token = data.get("idToken")
        
        try:
            decoded_token = auth.verify_id_token(id_token)
            request.session["user"] = decoded_token
            return JsonResponse({"message": "Login exitoso"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return render(request, "login/login.html")

def logout_view(request):
    request.session.flush()  # Elimina toda la sesión
    return render(request, "login/logout.html")

def reset_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            link = auth.generate_password_reset_link(email)
            return JsonResponse({"message": "Correo enviado"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return render(request, "login/reset_password.html")

def register_view(request):
    return render(request, "login/register.html")

