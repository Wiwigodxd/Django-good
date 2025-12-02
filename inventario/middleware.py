from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from .models import InicioSesion
import json

class RegistrarInicioSesionMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Detectamos cuando JWT responde con token
        if request.path == "/api/token/" and response.status_code == 200:
            try:
                data = json.loads(response.content.decode())
                # Extraemos username desde request
                body = json.loads(request.body.decode())
                username = body.get("username")

                user = User.objects.filter(username=username).first()
                if user:
                    InicioSesion.objects.create(usuario=user)
            except Exception:
                pass

        return response
