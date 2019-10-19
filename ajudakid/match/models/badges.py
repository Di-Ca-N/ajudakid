from django.db import models

class Badges(models.Model):
	icone = models.FileField()
	nome = models.CharField(max_length=30)
	descricao = models.TextField()
	apoiadores = models.ManyToManyField(ApoiadorPerfil, related_name="badges")