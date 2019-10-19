from django.contrib import admin
from match.models import AcaoApoiador, Acao, Apoiador, Badges, Entidade

# Register your models here.
admin.site.register(Apoiador)
admin.site.register(Entidade)
admin.site.register(Badges)
admin.site.register(Acao)
admin.site.register(AcaoApoiador)