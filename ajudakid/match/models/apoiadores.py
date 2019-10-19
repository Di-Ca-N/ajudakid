from django.db import models
from django.contrib.auth.models import User 

class Apoiador(models.Model):
	owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	tipo = models.CharField(max_length=2, choices=(
		('pf','Pessoa Física' ),
		('pj','Pessoa Jurídica')
		))
	registro = models.CharField(max_length=13)
	endereco = models.CharField(max_length=90)
	pontos = models.IntegerField()