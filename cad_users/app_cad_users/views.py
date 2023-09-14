from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.id_usuario = request.POST.get('id')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    return render(request,'usuarios/usuarios.html', usuarios)
    
    
    
