from django import forms
from .models import Entidade, Apoiador, Endereco
from django.contrib.auth.models import User


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
		exclude = ('pontos', 'badges', 'owner',)
		widgets = {
			'nome': forms.TextInput(attrs={'class':''}),
			'endereco': forms.TextInput(attrs={'class':''}),
			'registro': forms.TextInput(attrs={'class':''}),
		}
