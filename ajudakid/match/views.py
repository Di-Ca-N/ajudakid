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