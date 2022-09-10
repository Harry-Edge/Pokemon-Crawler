from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
import json
import concurrent.futures
from .crawler import PokemonCrawler


class GetAndUpdatePokemon(APIView):

    @staticmethod
    def get(request):
        """
        Calls the class to update and get new Pokemon data
        """

        crawler = PokemonCrawler()
        ran_successfully = crawler.run()

        if ran_successfully:
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
        return Response({'response': 'bad'}, status=status.HTTP_400_BAD_REQUEST)