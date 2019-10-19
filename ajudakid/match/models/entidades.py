from django.db import models
from .enderecos import Endereco
from django.contrib.auth.models import User 

class Entidade(models.Model):
	owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50)
	email = models.EmailField()
	cnpj = models.CharField(max_length=13)
	endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
