# -*- coding: utf-8 -*-
"""

"""

from Player.py import Player

influence_deck = []

def print_menu_and_select():
    print ("\nSelecciona una opción:")
    print ("0. Salir")
    return int(input())
    
def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break

if __name__ == "__main__":
    menu()