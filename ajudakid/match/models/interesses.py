from django.db import models


class Interesse(models.Model):
	nome = models.CharField(max_length=130)

	def __str__(self):
		return self.nome
