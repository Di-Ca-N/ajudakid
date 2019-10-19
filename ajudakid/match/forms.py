from django import forms
from .models.entidades import Entidade
from .models.apoiadores import Apoiador
from django.contrib.auth.models import User


class EntidadeForm(forms.ModelForm):
	class Meta:
		model = Entidade
		widgets = {
			'nome': forms.TextInput(attrs={'class':''}),
			'username': forms.TextInput(attrs={'class':''}),
			'email': forms.EmailInput(attrs={'class':''}),
			'endereco': forms.TextInput(attrs={'class':''}),
			'cnpj': forms.TextInput(attrs={'class':''}),
			'senha': forms.PasswordInput(attrs={'class':''}),
			'confirmacao_senha': forms.PasswordInput(attrs={'class':''}),
		}


class ApoiadorForm(ModelForm):
	class Meta:
		model = Apoiador
		exclude = (pontos, badges)
		widgets = {
			'nome': forms.TextInput(attrs={'class':''}),
			'username': forms.TextInput(attrs={'class':''}),
			'email': forms.EmailField(attrs={'class':''}),
			'senha': forms.PasswordInput(attrs={'class':''}),
			'confirmacao_senha': forms.PasswordInput(attrs={'class':''}),
			'endereco': forms.TextInput(attrs={'class':''}),
			'registro': forms.TextInput(attrs={'class':''}),
			'tipo': forms.ChoiceWidget(attrs={'class':''}),
		}
