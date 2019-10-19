from django import forms
from django.contrib.auth.models import User

from .models import Entidade, Apoiador, Endereco, AcaoApoiador

class EntidadeForm(forms.ModelForm):
	class Meta:
		model = Entidade
		exclude = ['owner', 'endereco']
		# widgets = {
		# 	'nome': forms.TextInput(attrs={'class':''}),
		# 	'endereco': forms.TextInput(attrs={'class':''}),
		# 	'cnpj': forms.TextInput(attrs={'class':''}),
		# }

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = '__all__'

class ApoiadorForm(forms.ModelForm):
	class Meta:
		model = Apoiador
		exclude = ('pontos', 'badges', 'owner', 'endereco')
		widgets = {
			'nome': forms.TextInput(attrs={'class':''}),
			'registro': forms.TextInput(attrs={'class':''}),
		}

class AcaoApoiadorForm(forms.ModelForm):
	class Meta:
		model = AcaoApoiador
		exclude = ('entidade', )
