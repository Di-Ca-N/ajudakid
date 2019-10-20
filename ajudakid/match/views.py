from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import EntidadeForm, ApoiadorForm, EnderecoForm, AcaoApoiadorForm, MyUserCreationForm
from .models import Apoiador, Entidade, Badge


def quem_somos(request):
	context = {}
	return render(request, 'match/quem_somos.html', context)

def entidades(request):
	entidades = Entidade.objects.all()
	return render(request, 'match/entidades.html', {'entidades': entidades})


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
			return redirect('match:ranking')

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
			acao.entidade = request.user.entidade
			if acao.valor >= 500 and acao.tipo == "d":
				acao.apoiador.badges.add(Badge.objects.get(pk=2))
				acao.apoiador.save()
			
			if acao.valor >= 50 and acao.tipo == 'v':
				acao.apoiador.badges.add(Badge.objects.get(pk=1))
				acao.apoiador.save()

			acao.save()
			return redirect('match:ranking')
	else:
		form = AcaoApoiadorForm()
	return render(request, 'match/cadastrar.html', {'forms': [form]})


def view_perfil(request, tipo, perfil_id):
	if tipo == 'apoiador':
		perfil = Apoiador.objects.get(id=perfil_id)
		instituicoes_apoiadas = Entidade.objects.filter(id__in=perfil.acoes.values('entidade'))
		parceiros = Entidade.objects.filter(interesses__in=perfil.interesses.all(), endereco__estado=perfil.endereco.estado).exclude(id__in=instituicoes_apoiadas.values_list('id', flat=True)).distinct()
		endereco = None

	else:
		perfil = Entidade.objects.get(id=perfil_id)
		parceiros = None
		instituicoes_apoiadas = None
		endereco = perfil.endereco

	return render(request, 'match/perfil.html', {'perfil': perfil, 'parceiros': parceiros, 'instituicoes_apoiadas': instituicoes_apoiadas, 'endereco': endereco})


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

