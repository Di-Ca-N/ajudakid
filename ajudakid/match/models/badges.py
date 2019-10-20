from django.db import models
from .apoiadores import Apoiador

class Badge(models.Model):
	icone = models.FileField()
	nome = models.CharField(max_length=30)
	descricao = models.TextField()
	apoiadores = models.ManyToManyField(Apoiador, related_name="badges", blank=True)
