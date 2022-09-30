from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'usuario', 'data_evento', )

admin.site.register(Evento, EventoAdmin)
