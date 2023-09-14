from django.urls import path
from app_cad_users import views

urlpatterns = [
    path('',views.home, name='nome'),
    path('usuarios/',views.usuarios, name='listagem_usuarios'),
]
