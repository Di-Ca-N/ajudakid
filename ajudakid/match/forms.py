from django import forms
from django.contrib.auth.models import User

from .models import Entidade, Apoiador, Endereco, AcaoApoiador

class EntidadeForm(forms.ModelForm):
	class Meta:
		model = Entidade
		exclude = ['owner', 'endereco']
		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Seu nome'}),
			'endereco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}),
			'cnpj': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CNPJ'}),
		}

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = '__all__'

class ApoiadorForm(forms.ModelForm):
	class Meta:
		model = Apoiador
		exclude = ('pontos', 'badges', 'owner', 'endereco')
		widgets = {
			'nome': forms.TextInput(attrs={'class':'', 'placeholder':'Seu nome'}),
			'registro': forms.TextInput(attrs={'class':'', 'placeholder':'CNPJ/CPF'}),
		}

class AcaoApoiadorForm(forms.ModelForm):
	class Meta:
		model = AcaoApoiador
		exclude = ('entidade', )
		widgets = {
			'nome' : forms.TextInput(attrs={'class':'form-control'}),
			'tipo' : forms.ChoiceField(),
			'valor' : forms.IntegerField(),
			'apoiador' : forms.ChoiceField(),

		}

