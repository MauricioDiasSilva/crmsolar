



from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Projeto
from .forms import ClienteForm, ProjetoForm

def home(request):
    return render(request, 'solar/home.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'solar/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'solar/detalhe_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solar/lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'solar/criar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('solar/lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'solar/editar_cliente.html', {'form': form})

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'solar/lista_projetos.html', {'projetos': projetos})

def detalhe_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'solar/detalhe_projeto.html', {'projeto': projeto})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solar/lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'solar/criar_projeto.html', {'form': form})

def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('solar/lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'solar/editar_projeto.html', {'form': form})