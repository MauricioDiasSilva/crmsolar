from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
