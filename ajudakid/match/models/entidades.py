from django.db import models
from django.contrib.auth.models import User 

class Entidade(models.Model):
	owner = models.OneToOneField('auth.User')
	nome = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	cnpj = models.CharField(max_length=13)
	endereco = models.CharField(max_length=90)