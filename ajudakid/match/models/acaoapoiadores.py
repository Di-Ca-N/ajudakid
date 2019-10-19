from django.db import models
from .acoes import Acao
from .apoiadores import Apoiador
from .entidades import Entidade

class AcaoApoiador(models.Model):
	acao = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name="apoiadores")
	apoiadores = models.ForeignKey(Apoiador, on_delete=models.CASCADE, related_name="acoes")
	entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name="acoes")
