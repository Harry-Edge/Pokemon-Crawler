# Pokemon API Crawler

This is a simple crawler that crawls the [Pokemon API](https://pokeapi.co/) for Pokemon

Had to use threading to speed up the process of requests. Although issue with that is the data on the DB is not stored in order compared to the API,
Although this is mitigated by ordering the data by the api_id field.

Design on the frontend could be better if the site wasn't forced to reload after the API call is finished.

Test is done on all methods of crawler class, and also checking if the API and index view return 200 status code.

Can only scale to checking if a 1000 Pokemon exist without changing the code. Will still call after 905 Pokemon even no more exist currently 
