from main.models import Pokemon
import requests
import json
import concurrent.futures


class PokemonCrawler:
    def __init__(self, ) -> None:
        self.url_endpoint: str = 'https://pokeapi.co/api/v2/pokemon-species/'

    def get_individual_pokemon(self, pokemon_id: int):
        """
        Gets the Pokemon data from the API
        """
        url = f"{self.url_endpoint}{pokemon_id}"

        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)

            return {
                'id': data['id'], 'name': data['name'], 'is_legendary': data['is_legendary'],
                'is_mythical': data['is_mythical'], 'description': data['flavor_text_entries'][0]['flavor_text']
            }
        return None

    def get_all_pokemon(self) -> list:
        """
        Uses threading to call the API for each Pokemon in the range of 1 to 10
        :return: list of dictionaries containing the Pokemon ID and Name
        """

        pokemon_data = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(self.get_individual_pokemon, _i) for _i in range(1, 1000)]
            for f in concurrent.futures.as_completed(results):
                if f.result():
                    pokemon_data.append(f.result())

        return pokemon_data

    @staticmethod
    def add_new_pokemon(pokemon_data: dict) -> None:
        """
        Adds a new Pokemon to the database
        """
        Pokemon.objects.create(
            api_id=pokemon_data['id'],
            name=pokemon_data['name'],
            is_legendary=pokemon_data['is_legendary'],
            is_mythical=pokemon_data['is_mythical'],
            description=pokemon_data['description']
        )

    @staticmethod
    def update_existing_pokemon(pokemon_data: dict) -> None:
        """
        Updates an existing Pokemon in the database based on a dictionary
        """
        Pokemon.objects.filter(api_id=pokemon_data['id']).update(
            name=pokemon_data['name']
        )

    def run(self) -> bool:
        """
        Main function to run the crawler

        :return: True if successful, False if not
        """
        try:
            pokemon_data = self.get_all_pokemon()
            all_current_pokemon_data = Pokemon.objects.all()

            for pokemon in pokemon_data:
                """
                Checks if the Pokemon is already in the database. If so it then checks 
                to see if and data is changed if so it updates the data
    
                If the Pokemon is not in the database it adds it to the database
                """
                existing_pokemon = all_current_pokemon_data.filter(api_id=pokemon['id'])

                if existing_pokemon.exists():
                    # Check if the data has changed and update if so
                    if existing_pokemon[0].name != pokemon['name'] \
                            or existing_pokemon[0].is_legendary != pokemon['is_legendary'] \
                            or existing_pokemon[0].is_mythical != pokemon['is_mythical'] \
                            or existing_pokemon[0].description != pokemon['description']:
                        self.update_existing_pokemon(pokemon)
                else:
                    # Add the new Pokemon to the database
                    self.add_new_pokemon(pokemon)
            return True

        except Exception as e:
            print(e)
            return False
