from django.db import models

class Acao(models.Model):
	nome = models.CharField()
	tipo = models.CharField(max_length=1, choices=(
		('d','Doação' ),
		('v','Voluntariado')
		))