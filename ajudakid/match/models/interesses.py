from django.db import models
from .entidades import Entidade
from .apoiadores import Apoiador

class Interesse(models.Model):
	nome = models.CharField(max_length=130)
	tags = models.TextField() #Adicione as tags separadas por ";" sem aspas
	prop = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name="interesses", null=True)
	prop1 = models.ForeignKey(Apoiador, on_delete=models.CASCADE, related_name="interesses", null=True)