from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from django.http.response import HttpResponse as HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import RegistroUsuarioForm, LoginUsuarioForm
from django.contrib.auth import login, authenticate, login
#importar modelo
from django.contrib.auth.models import User 


def login_view(request):
    if request.method == "POST":
        form = LoginUsuarioForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)

                if user.check_password(password):
                    login(request, user)
                    messages.success(request, f"Usario{user.username} iniciado con exito")
                    return HttpResponseRedirect("/")
                else:
                    messages.error(request,"Contraseña incorrecta. Verifique sus credenciales")
            except User.DoesNoExist:
                messages.error(request, "El usuario con ese correo no existe")
            except Exception as e:
                messages.error(request, "Ocurrio un error. Intentelo  nuevamente")
        else:
            messages.error(request, "Formulario invalido, Por favor,  revise los campos")
    else:
        form = LoginUsuarioForm()    
    return render(request, 'usuarios/login.html', {'form': form})



def registro_view(request):
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Error al intentar registrar al usuario, por favor verifique los datos.")
            return render(request, 'usuarios/registro.html', {"form": form})
                
    else:
        form = RegistroUsuarioForm()
    return render(request,  'usuarios/registro.html', {"form": form})



class UserLogoutView(LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Ha cerrado la sesion exitosamente")
        return super().dispatch(request, *args, **kwargs)
