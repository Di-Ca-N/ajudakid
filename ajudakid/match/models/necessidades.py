from django.db import models
from .entidades import Entidade

class Necessidade(models.Model):
	nome = models.CharField(max_length=130)
	tags = models.TextField() #Adicione as tags separadas por ";" sem aspas
	entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name=necessidades)