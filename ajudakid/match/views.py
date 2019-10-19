from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

from .forms import EntidadeForm, ApoiadorForm, EnderecoForm, AcaoApoiadorForm
from .models import Apoiador

def quem_somos(request):
	context = {}
	return render(request, 'match/quem_somos.html', context)

def entidades(request):
	context = {}
	return render(request, 'match/entidades.html', context)

def ranking(request):
	rank = Apoiador.objects.all()
	for filter_field in ('pais', 'estado', 'cidade', 'bairro'):
		if request.GET.get(filter_field):
			rank = rank.filter(**{filter_field: request.GET.get(filter_field)})
	return render(request, 'match/rank.html', {'rank': rank})


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


@user_passes_test(lambda user: hasattr(user, 'entidade'))
def cadastrar_acao(request):
	if request.method == 'POST':
		form = AcaoApoiadorForm(request.POST)
		if form.is_valid():
			acao = form.save(commit=False)
			acao.entidade = request.user
			acao.save()
			return render(request, 'match/sucesso.html')
	else:
		form = AcaoApoiadorForm()
	return render(request, 'match/cadastrar.html', {'forms': [form]})

def view_perfil(request, perfil_id):
	perfil = Apoiador.objects.get(id=perfil_id)
	return render(request, 'match/perfil.html', {'perfil': perfil})
