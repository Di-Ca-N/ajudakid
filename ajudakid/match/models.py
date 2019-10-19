from django.db import models

class EntidadePerfil(models.Model):
	owner = models.OneToOne('auth.User')
	nome = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	cnpj = models.CharField(max_length=13)
	endereco = models.CharField(max_length=90)

class ApoiadorPerfil(models.Model):
	owner = models.OneToOne('auth.User')
	nome = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	tipo = models.CharField(max_length=2, choices=(
		('pf','Pessoa Física' ),
		('pj','Pessoa Jurídica')
		))
	registro = models.CharField(max_length=13)
	endereco = models.CharField(max_length=90)
	pontos = models.IntegerField()


class Badges(models.Model):
	icone = models.FileField()
	nome = models.CharField(max_length=30)
	descricao = models.TextField()
	apoiadores = models.ManyToManyField(ApoiadorPerfil, related_name="badges")

class Acao(models.Model):
	nome = models.CharField()
	tipo = models.CharField(max_length=1, choices=(
		('d','Doação' ),
		('v','Voluntariado')
		))

class AcaoApoiador(models.Model):
	acao = models.ForeignKey(Acao, on_delete=models.SET_NULL, related_name="apoiadores")
	apoiadores = models.ForeignKey(ApoiadorPerfil, on_delete=models.CASCADE, related_name="acoes")
	entidade = mdoels.Foreignkey(EntidadePerfil, on_delete=models.SET_NULL, related_name="acoes")
