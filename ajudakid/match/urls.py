from django.urls import path
from . import views 

app_name = 'match'

urlpatterns = [
	path('quem_somos/', views.quem_somos, name='quem_somos'),
	path('entidades/', views.entidades, name='entidades'),
	path('ranking/', views.ranking, name='ranking'),
	path('cadastrar/', views.cadastrar, name='cadastro'),
	path('cadastrar/entidades/', views.cadastrar_entidades, name='cadastro_entidade'),
	path('cadastrar/apoiador/', views.cadastrar_apoiador, name='cadastro_apoiador'),
	]