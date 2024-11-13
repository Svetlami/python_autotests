import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b62f97d9a79b58a0929894683d51cc31'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_pokemons = {
    "pokemon_id": "129806"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
 print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemons)
print(response.text)
