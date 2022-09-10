from django.urls import path
from .views import GetAndUpdatePokemon

urlpatterns = [
    path('get-and-update-pokemon/', GetAndUpdatePokemon.as_view()),
]