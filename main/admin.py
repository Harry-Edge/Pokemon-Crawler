from django.contrib import admin
from .models import *


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_id', 'is_legendary', 'is_mythical')
    search_fields = ['name', 'api_id']
