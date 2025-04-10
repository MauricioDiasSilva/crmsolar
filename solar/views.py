from django.shortcuts import render
from .models import Cliente, Projeto

def home(request):
    return render(request, 'solar/home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'solar/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'solar/detalhe_cliente.html', {'cliente': cliente})

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'solar/lista_projetos.html', {'projetos': projetos})

def detalhe_projeto(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    return render(request, 'solar/detalhe_projeto.html', {'projeto': projeto})