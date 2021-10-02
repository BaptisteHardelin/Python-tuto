import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

def read_character_from_json():
    values = []
    with open('character.json') as f:
        data = json.load(f)

    for entry in data:
        values.append(entry['character'])

    return values

def read_quote_from_json():
    values = []
    with open('quotes.json') as f:
        data = json.load(f)

    for entry in data:
        values.append(entry['quote'])

    return values

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item

def random_character():
    all_values = read_character_from_json()
    return get_random_item_in(all_values)

def random_quote():
    all_values = read_quote_from_json()
    return get_random_item_in(all_values)


# Programm
user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.\n")

while user_answer != "B":
    print(message(random_character(), random_quote()))
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.\n")