# -*- coding: utf-8 -*-
"""

"""

from Player import Player

players = []
influence_deck = []

def create_player():
    name = input("ingresa el nombre del jugador ")
    coins = 2
    #falta que el jugador reciba dos influencias de influence_deck
    players.append(Player(name, influence, coins))

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

# crear funcion que muestre influencias del jugador en turno y coins del resto
# crear fx que muestre cada accion
# crear menu que permita seleccionar acciones y dar la oportunidad a los demas
# de desafiarla o contraatacarla
# crear log del turno

if __name__ == "__main__":
    initial_menu()