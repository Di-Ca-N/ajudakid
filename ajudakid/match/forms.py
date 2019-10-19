from django import forms
from .models.entidades import Entidade
from .models.apoiadores import Apoiador
from django.contrib.auth.models import User


class EntidadeForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':''}))
	endereco = forms.CharField()
	cnpj = forms.CharField()

	class Meta:
		model = Entidade
		widgets = {
			'nome': forms.TextInput(attrs={'class':''}),
			'username': ,
			'email': forms.EmailInput(attrs={'class':''}),
			'endereco': forms.TextInput(attrs={'class':''}),
			'cnpj': forms.TextInput(attrs={'class':''}),
			'senha': forms.PasswordInput(attrs={'class':''}),
			'confirmacao_senha': forms.PasswordInput(attrs={'class':''}),
		}

	def clean(self):
		super().clean()
		username = self.cleaned_data['username']
		if username in User.objects.values_list('username', flat=True):
			self.add_error('username', error_message='Esse nome de usuário já existe.')

	def save(self, commit=True):
		username = self.cleaned_data['username']
		user = User.objects.create_user(username)

		nome = self.cleaned_data['nome']
		email = self.cleaned_data['email']
		endereco = self.cleaned_data['endereco']
		cnpj = self.cleaned_data['cnpj']
		senha = self.cleaned_data['senha']
		confirmacao_senha = self.cleaned_data['confirmacao_senha']

		Entidade.objects.create(owner=user, nome=nome, endereco=endereco, cnpj=cnpj)

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

	def clean(self):
		super().clean()
		username = self.cleaned_data['username']
		if username in User.objects.values_list('username', flat=True):
			self.add_error('username', error_message='Esse nome de usuário já existe.')

	def save(self, commit=True):
		username = self.cleaned_data['username']
		user = User.objects.create_user(username)

		nome = self.cleaned_data['nome']
		email = self.cleaned_data['email']
		endereco = self.cleaned_data['endereco']
		cnpj = self.cleaned_data['cnpj']
		senha = self.cleaned_data['senha']
		confirmacao_senha = self.cleaned_data['confirmacao_senha']
		registro = 
		tipo = self.cleaned_data[]

		Apoiador.objects.create(owner=user, nome=nome, email=email)
