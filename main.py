# -*- coding: utf-8 -*-
"""

"""
from numpy import random
from Player import Player

players = []
def shuffle_deck():
    deck = ["Duque", "Duque", "Duque", "Asesino", "Asesino", "Asesino", 
    "Capitán", "Capitán", "Capitán", "Embajador", "Embajador", "Embajador", 
    "Condesa", "Condesa", "Condesa"]
    random.shuffle(deck)
    return deck

influence_deck = shuffle_deck()

def create_player():
    name = input("ingresa el nombre del jugador ")
    coins = 2
    influence = []
    influence.append(influence_deck[0])
    influence_deck.pop(0)
    influence.append(influence_deck[0])
    influence_deck.pop(0)
    #falta que el jugador reciba dos influencias de influence_deck
    players.append(Player(name, influence, coins))

def show_game_status():
    print("\nJugadores creados:")
    for (i, _) in enumerate(players):
        print(f"{i+1}: {players[i].name} - {players[i].influence} - {players[i].coins}monedas")

def print_menu_and_select():
    print ("\nSelecciona una opción:")
    print ("1. Ingresar un jugador")
    print ("0. Salir")
    return int(input())
    
def initial_menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            create_player()
        show_game_status()
            
            

# crear funcion que muestre influencias del jugador en turno y coins del resto
# crear fx que muestre cada accion
# crear menu que permita seleccionar acciones y dar la oportunidad a los demas
# de desafiarla o contraatacarla
# crear log del turno

if __name__ == "__main__":
    initial_menu()