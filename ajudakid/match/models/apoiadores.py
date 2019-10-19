from django.db import models
from django.contrib.auth.models import User 
from .enderecos import Endereco

class Apoiador(models.Model):
	owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50)
	email = models.EmailField()
	tipo = models.CharField(
		max_length=2, 
		choices=(
			('pf','Pessoa Física' ),
			('pj','Pessoa Jurídica')
		)
	)
	registro = models.CharField(max_length=13, help_text='CPF, se pessoa física. CNPJ, se jurídica')
	endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
	pontos = models.IntegerField(default=0)

	def __str__(self):
		return self.nome

	def calc_pontuacao(self):
		self.pontos = sum([action.get_pontuacao() for action in self.acoes.all()])
		self.save()
		return self.pontos
