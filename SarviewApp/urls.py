from re import template
from django.urls import path
from SarviewApp import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', LoginView.as_view(template_name="SarviewApp/login.html"), name="login"), #Ventana de login
    path('lista/', login_required(views.lista), name="lista"), #Ventana de lista de maquinas
    path('rodion/', login_required(views.rodion), name="rodion"), #Ventana de visualización de Rodion
    path('register/', login_required(views.register), name="register"), #Ventana de registro 
    path('logout/', LogoutView.as_view(template_name="SarviewApp/logout.html"), name="logout"), #Ventana de logout con funcionalidad de logout
    path('simulacion/', login_required(views.simulacion), name="simulacion"), #Ventana de visualización de datos de simulación.
    path('dashboard/', login_required(views.dashboard), name="dashboard"), #Ventana de visualización de datos de simulación versión nueva.
]