import os
import sys
import json
from pokemon import Pokemon

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# 1. Oppsett
# Åpner json-fila og putter innholdet i variabelen data:
with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

pokemon = []
for pokemon_ordbok in pokemon:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon.append(ny_pokemon)

print(" -- Pokémon -- ")

while True:
    rens_terminal()
    print(" -- Pokémon -- ")
    print("1 - Pokémon")
    print("2 - Trainers")
    print("3 - Create Trainer")
    print("4 - Exit")
    brukervalg = input("> ")

    if brukervalg == "1":
        print("pokemonoversikt")
        for pokemon in pokemon:
            print(pokemon)
        input("Press 'ENTER' to exit to main menu")
    if brukervalg == "2":
        print("Closing...")
        break
    else:
        print("Ugyldig input")
        input("Press 'ENTER' to exit to main menu")