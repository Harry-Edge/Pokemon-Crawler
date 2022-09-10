from django.test import TestCase
from .crawler import PokemonCrawler
from main.models import Pokemon


class TestPokemonCrawler(TestCase):
    def test_return_individual_pokemon(self):
        pokemon_crawler = PokemonCrawler()
        pokemon = pokemon_crawler.get_individual_pokemon(1)

        self.assertEqual(pokemon['id'], 1)
        self.assertEqual(pokemon['name'], 'bulbasaur')
        self.assertEqual(pokemon['is_legendary'], False)
        self.assertEqual(pokemon['is_mythical'], False)

    def test_return_all_pokemon(self):
        pokemon_crawler = PokemonCrawler()
        pokemon_data = pokemon_crawler.get_all_pokemon()

        self.assertEqual(len(pokemon_data), 905)

    def test_add_new_pokemon(self):
        pokemon_crawler = PokemonCrawler()
        pokemon_data = pokemon_crawler.get_individual_pokemon(1)
        pokemon_crawler.add_new_pokemon(pokemon_data)
        pokemon = Pokemon.objects.get(api_id=1)

        self.assertEqual(pokemon.api_id, 1)
        self.assertEqual(pokemon.name, 'bulbasaur')
        self.assertEqual(pokemon.is_legendary, False)
        self.assertEqual(pokemon.is_mythical, False)

    def test_update_existing_pokemon(self):
        pokemon_crawler = PokemonCrawler()
        pokemon_data = pokemon_crawler.get_individual_pokemon(1)
        pokemon_crawler.add_new_pokemon(pokemon_data)
        pokemon_data['name'] = 'new name'
        pokemon_crawler.update_existing_pokemon(pokemon_data)
        pokemon = Pokemon.objects.get(api_id=1)

        self.assertEqual(pokemon.api_id, 1)
        self.assertEqual(pokemon.name, 'new name')
        self.assertEqual(pokemon.is_legendary, False)
        self.assertEqual(pokemon.is_mythical, False)


class TestAPIView(TestCase):
    def test_api(self):
        response = self.client.get('/api/get-and-update-pokemon/')
        self.assertEqual(response.status_code, 200)