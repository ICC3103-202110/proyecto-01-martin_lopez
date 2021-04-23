# -*- coding: utf-8 -*-
"""

"""
from numpy import random
from Player import Player
#from Character import Character

players = []
def shuffle_deck(): #baraja las cartas de manera aleatoria
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
    players.append(Player(name, influence, coins))

def show_game_status(): #muestra fluencia y monedas de todos los jugadores
    print("\nSituación Jugadores:")
    for (i, _) in enumerate(players):
        print(f"{i+1}: {players[i].name} le quedan {len(players[i].influence)} de fluencia y {players[i].coins} monedas")

def print_menu_and_select():
    print ("\nSelecciona una opción:")
    print ("1. Ingresar un jugador")
    print ("0. Comenzar el juego")
    return int(input())

def print_actions_and_select():
    print ("\nSeleccione una acción o carta a jugar:")
    print ("1. Ingresos")
    print ("2. Ayuda Extranjera")
    print ("3. Golpe")
    print ("4. Duque")
    print ("5. Asesino")
    print ("6. Capitán")
    print ("7. Embajador")
    return int(input())

def show_my_characters():
    print ("\n¿Desea mirar sus cartas?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def show_log_game():
    print ("\n¿Desea ver el log del juego?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def other_players_turn():
    a = [] 
    for k in range(len(players)):
        a.append(players[k].name) #lista con los jugadores
    return a

def challenge_player():
    print ("\n¿Desafiar jugador?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def initial_menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        if selection == 1:
            create_player()
        if len(players) == 4: #si se ingresaron 4 jugadores el juego parte automáticamente
            break

def initialize_game():
    log=[]
    shift_counter = 0 #contador de turnos
    while True: #ciclo hasta que termine el juego
        shift_counter += 1 
        log.append("Turno "+str(shift_counter)) #agrega contador de turnos al log del juego
        turned_around_characters = []
        for i in range(len(players)): #un turno
            show_game_status() #muestra estado actual del juego antes de que comienze el turno de un jugador
            print (turned_around_characters)
            print ("\n"+"¡Juega "+players[i].name+"!")
            show_characters = show_my_characters() #si el jugador quiere ver sus cartas
            if show_characters == 1:
                print("\nTus cartas son:")
                for j in players[i].influence:
                    print (j)
            other_players = other_players_turn()
            other_players.pop(i) #lista de jugadores que no es su turno
            random.shuffle(other_players) #de esta manera el desafio o contraataque será de manera aleatoria si ambos quieren desafiar
            action = print_actions_and_select()
            if action == 1:
                log.append(players[i].name+" obtiene 1 moneda por Ingresos") #no puede ser desafiado ni contraatacado
            if action == 2:
                pass
            if action == 3:
                log.append(players[i].name+" paga 7 monedas y realiza un Golpe") #no puede ser desafiado ni contraatacado
            if action == 4:
                print (players[i].name+" utiliza Duque")
                log.append(players[i].name+" utiliza Duque")
                for l in other_players:
                    print (l)
                    challenge = challenge_player()
                    if challenge == 1:
                        print (l+" desafía a "+players[i].name)
                        log.append(l+" desafía a "+players[i].name)
                        for j in players[i].influence:
                            if j == "Duque":
                                print (players[i].name+" tiene la carta Duque")
                                print (l+" elige que carta dar vuelta:")
                                pass                      
                        break
                pass
            if action == 5:
                pass
            if action == 6:
                pass
            if action == 7:
                pass
        log.append(" ") #agrega un espacio para diferenciar los turnos
        show_log = show_log_game()
        if show_log == 1: #muestra el log de todos los turnos
            for t in range(len(log)):
                print (log[t])
        
        if len(players) == 1: #solo queda un jugador, termina el juego.
            break

            

# si el jugador comienza el turno con 10 monedas, esta obligado a ejecutar coup. agregarlo
# crear menu que permita seleccionar acciones [LISTO] y dar la oportunidad a los demas
# de desafiarla o contraatacarla 
# hacer conexión entre las acciones de character con main
# crear un sistema en que otros jugadores puedan desafiar o contraatacar


if __name__ == "__main__":
    initial_menu()
    initialize_game()