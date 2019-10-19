from django.db import models

class AcaoApoiador(models.Model):
	acao = models.ForeignKey(Acao, on_delete=models.SET_NULL, related_name="apoiadores")
	apoiadores = models.ForeignKey(ApoiadorPerfil, on_delete=models.CASCADE, related_name="acoes")
	entidade = models.ForeignKey(EntidadePerfil, on_delete=models.SET_NULL, related_name="acoes")
