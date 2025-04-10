from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Adiciona a página principal
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:projeto_id>/', views.detalhe_projeto, name='detalhe_projeto'),
]