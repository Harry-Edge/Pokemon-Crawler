from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Pokemon


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):

        all_pokemon = Pokemon.objects.all().order_by('api_id')

        return render(request, self.template_name, context={'all_pokemon': all_pokemon})

    @staticmethod
    def post(request):
        """
        Only one submit button on the page, so this is the only post method that will be called

        """
        Pokemon.objects.all().delete()
        return redirect('index')