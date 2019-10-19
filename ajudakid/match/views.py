from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import EntidadeForm, ApoiadorForm, EnderecoForm

def quem_somos(request):
	return HttpResponse("Olá")

def entidades(request):
	return HttpResponse("Olá")

def ranking(request):
	return HttpResponse("Olá")

def cadastrar(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('match:sucesso_cadastro')
	else:
		form = UserCreationForm()
	
	return render(request, 'match/cadastrar.html', {'forms': [form]})

def cadastrar_entidades(request):
	if request.method == 'POST':
		form = EntidadeForm(request.POST)
		endereco_form = EnderecoForm(request.POST)

		if form.is_valid() and endereco_form.is_valid():
			endereco = endereco_form.save()
			entidade = form.save(commit=False)

			entidade.owner = request.user
			entidade.endereco = endereco
			entidade.save()

			return redirect('match:sucesso_cadastro')
	else:
		form = EntidadeForm()
		endereco_form = EnderecoForm()
	return render(request, 'match/cadastrar.html', {'forms': [form, endereco_form]})

def cadastrar_apoiador(request):
	if request.method == 'POST':
		form = ApoiadorForm(request.POST)
		endereco_form = EnderecoForm(request.POST)

		if form.is_valid() and endereco_form.is_valid():
			apoiador = form.save(commit=False)
			endereco = endereco_form.save()

			apoiador.owner = request.user
			apoiador.endereco = endereco

			apoiador.save()
			return redirect('match:sucesso_cadastro')

	else:
		form = ApoiadorForm()
		endereco_form = EnderecoForm()
	
	return render(request, 'match/cadastrar.html', {'forms': [form, endereco_form]})

def sucesso_cadastro(request):
	return HttpResponse("Olá")

def cadastrar_acao(request):
	return HttpResponse("None")
''' from django.shortcuts import render
from models import Entidade
from models import Apoiadores
from .forms import Formulario

def home(request):
	context = {}
	return render(request, 'home/index.html', context)

def quem_somos(request):
	context = {}
	return render(request, 'quem_somos/index.html', context)

def entidades(request):
	context = {'entidades':Entidade.objects.all()}
	return render(request, 'entidades/index.html', context)

def ranking(request):
	context = {'classificados': Apoiadores.objects.all()}
	return render(request, 'ranking/index.html', context)

def cadastro_apoiador(request):
	if request.method == "POST":
		form = Formulario(request.POST)
		
		if form.is_valid():
			user = form.save()
			#------------VERIFICAR----------------

			return render(request, 'login/login.html', )
	else:
		context = {'form': Formaulario()}
		return render(request, 'cadastro_apoiador/index.html', context)

def cadastro_entidade(request):
	if request.method == "POST":
		form = Formulario(request.POST)
		
		if form.is_valid():
			user = form.save()
			#------------VERIFICAR----------------

			return render(request, 'login/login.html', )
	else:
		context = {'form': Formaulario()}
		return render(request, 'cadastro_aentidade/index.html', context)

'''