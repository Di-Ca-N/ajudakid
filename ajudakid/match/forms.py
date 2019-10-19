from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Entidade, Apoiador, Endereco, AcaoApoiador

class EntidadeForm(forms.ModelForm):
	class Meta:
		model = Entidade
		exclude = ['owner', 'endereco']
		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Seu nome'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'cnpj': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CNPJ'}),
			'descricao':forms.TextInput(attrs={'class':'form-control'}),
			'interesses':forms.SelectMultiple(attrs={'class':'form-control'}),
		}

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = '__all__'
		widgets = {
			'estado': forms.Select(attrs={'class': 'form-control'}),
			'pais': forms.HiddenInput(),
			'cidade': forms.TextInput(attrs={'class': 'form-control'}),
			'bairro': forms.TextInput(attrs={'class': 'form-control'}),
			'rua': forms.TextInput(attrs={'class': 'form-control'}),
			'numero': forms.TextInput(attrs={'class': 'form-control'}),
			'complemento': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ApoiadorForm(forms.ModelForm):
	class Meta:
		model = Apoiador
		exclude = ('pontos', 'badges', 'owner', 'endereco')
		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Seu nome'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'tipo': forms.Select(attrs={'class':'form-control'}),
			'registro': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CNPJ/CPF'}),
			'descricao':forms.TextInput(attrs={'class':'form-control'}),
			'interesses':forms.SelectMultiple(attrs={'class':'form-control'}),
		}

class AcaoApoiadorForm(forms.ModelForm):
	class Meta:
		model = AcaoApoiador
		exclude = ('entidade', )
		widgets = {
			'nome' : forms.TextInput(attrs={'class':'form-control'}),
		}


class MyUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control'})
		self.fields['password1'].widget.attrs.update({'class': 'form-control'})
		self.fields['password2'].widget.attrs.update({'class': 'form-control'})
