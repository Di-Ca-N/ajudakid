from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import EntidadeForm, ApoiadorForm, EnderecoForm, AcaoApoiadorForm, MyUserCreationForm
from .models import Apoiador, Entidade


def quem_somos(request):
	context = {}
	return render(request, 'match/quem_somos.html', context)

def entidades(request):
	context = {}
	return render(request, 'match/entidades.html', context)


def ranking(request):
	rank = Apoiador.objects.order_by('-pontos')
	for filter_field in ('endereco__estado', 'endereco__cidade', 'endereco__bairro'):
		if request.GET.get(filter_field):
			rank = rank.filter(**{filter_field: request.GET.get(filter_field)})
	return render(request, 'match/ranking.html', {'ranking': rank})


def cadastrar(request):
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('match:sucesso_cadastro')
	else:
		form = MyUserCreationForm()
	
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

			return redirect('match:perfil')
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
			return redirect('match:perfil')

	else:
		form = ApoiadorForm()
		endereco_form = EnderecoForm()
	
	return render(request, 'match/cadastrar.html', {'forms': [form, endereco_form]})

def sucesso_cadastro(request):
	return render(request, 'match/sucesso.html')


@user_passes_test(lambda user: hasattr(user, 'entidade'))
def cadastrar_acao(request):
	if request.method == 'POST':
		form = AcaoApoiadorForm(request.POST)
		if form.is_valid():
			acao = form.save(commit=False)
			acao.entidade = request.user
			acao.save()
			return redirect('match/perfil')
	else:
		form = AcaoApoiadorForm()
	return render(request, 'match/cadastrar.html', {'forms': [form]})


@login_required
def view_perfil(request, tipo, perfil_id):
	if tipo == 'apoiador':
		perfil = Apoiador.objects.get(id=perfil_id)
		parceiros = Entidade.objects.filter(interesses__in=perfil.interesses.all())
		instituicoes_apoiadas = Entidade.objects.filter(id__in=perfil.acoes.values('entidade'))

	else:
		perfil = Entidade.objects.get(id=perfil_id)
		parceiros = Apoiador.objects.filter(interesses__in=perfil.interesses.all())
		instituicoes_apoiadas = None

	return render(request, 'match/perfil.html', {'perfil': perfil, 'parceiros': parceiros, 'instituicoes_apoiadas': instituicoes_apoiadas})


@login_required
def relacionar(request):
	try:
		pessoas = Apoiador.object.all()
		interesses = request.user.entidade.interesses

	except:
		pessoas = Entidade.object.all()
		interesses = request.user.apoiadores.interesses
	
	relacionados = []

	geral = ""
	for x in interesses:
		geral += x.tags

	for y in pessoas:
		interesse = y.interesses.tags.split(';')
		for z in interesse:
			if z in geral:
				relacionados.append(y)
	
	return relacionados

