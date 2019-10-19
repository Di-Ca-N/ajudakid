from django.shortcuts import render

def home(request):
	context = {}
	return render(request, 'home/index.html', context)

def quem_somos(request):
	context = {}
	return render(request, 'quem_somos/index.html', context)

def entidades(request):
	context = {}
	return render(request, 'entidades/index.html', context)

def ranking(request):
	context = {}
	return render(request, 'ranking/index.html', context)