from django.shortcuts import render

def home(request):
	context = {}
	return render(request, 'ajudakid/base.html', context)