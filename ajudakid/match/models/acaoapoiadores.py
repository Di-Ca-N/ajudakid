from django.db import models

from .apoiadores import Apoiador
from .entidades import Entidade

class AcaoApoiador(models.Model):
	nome = models.CharField(max_length=50)
	tipo = models.CharField(max_length=1, choices=(
		('d','Doação' ),
		('v','Voluntariado')
	))
	valor = models.IntegerField(help_text="Valor doado ou horas trabalhadas")
	apoiador = models.ForeignKey(Apoiador, on_delete=models.CASCADE, related_name="acoes")
	entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name="acoes")
