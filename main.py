# -*- coding: utf-8 -*-
"""

"""
from numpy import random
from Player import Player
from Character import *

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
    coins = 4 #por mientras
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
    print ("0. Se jugó un golpe, terminar turno")
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

def challenge_player():
    print ("¿Desafiar jugador?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def counter_attack_player():
    print ("¿Contraatacar jugador?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def challenge_counter():
    print ("¿Desafiar el contraataque?")
    print ("1. Si")
    print ("2. No")
    return int(input())

def counter_attack(other_players):
    for l in range(len(other_players)): #todos los jugadores eligen si contraatacan o no, de manera aleatoria
        print ("\n"+other_players[l].name)
        counter = counter_attack_player()
        if counter == 1:
            print("\nTus cartas son:")
            for j in other_players[l].influence:
                print (j)
            challenge = challenge_counter()
            if challenge == 1:
                x += 1
            if challenge == 0:
                x = 0
                print ("Contraataque exitoso")
        

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
    turned_around_characters = []
    while True: #ciclo hasta que termine el juego
        shift_counter += 1 
        log.append("Turno "+str(shift_counter)) #agrega contador de turnos al log del juego
        for i in range(len(players)): #un turno
            if len(players[i].influence) < 1: #comprobar si al juagador le quedan fluencias
                print (players[i].name+" ha sido eliminado del juego")
                log.append(players[i].name+" ha sido eliminado del juego")
                players.pop(i)
                break
            show_game_status() #muestra estado actual del juego antes de que comienze el turno de un jugador
            print (turned_around_characters)
            print ("\n"+"¡Juega "+players[i].name+"!")
            show_characters = show_my_characters() #si el jugador quiere ver sus cartas
            if show_characters == 1:
                print("\nTus cartas son:")
                for j in players[i].influence:
                    print (j)
            if players[i].coins > 9: #si un jugador tiene 10 monedas o más debe hacer un golpe                
                Character.coup(i, other_players, log, turned_around_characters)
            other_players = players[:] #copia de la lista players
            other_players.pop(i) #lista de jugadores que no es su turno
            random.shuffle(other_players) #de esta manera el desafio o contraataque será de manera aleatoria si mas de uno quiere desafiar
            action = print_actions_and_select()
            if action == 1:
                Character.income(i, players) #Llamamos a la función de Character
                print (players[i].name+" obtiene 1 moneda por Ingresos.")
                log.append(players[i].name+" obtiene 1 moneda por Ingresos.") #no puede ser desafiado ni contraatacado
            if action == 2:
                Character.foreign_aid(i, players)
                print (players[i].name+" obtiene 2 monedas por Ayuda Extranjera")
                log.append(players[i].name+" obtiene 2 monedas por Ayuda Extranjera")
            if action == 3:
                Character.coup(i, other_players, log, turned_around_characters)
            if action == 4:
                print (players[i].name+" quiere utilizar Duque")
                log.append(players[i].name+" quiere utilizar Duque")
                for l in range(len(other_players)): #todos los jugadores eligen si desafian o no, de manera aleatoria
                    print ("\n"+other_players[l].name)
                    challenge = challenge_player()
                    condition = 0
                    if challenge == 1:
                        print (other_players[l].name+" desafía a "+players[i].name)
                        log.append(other_players[l].name+" desafía a "+players[i].name)
                        if players[i].influence.count("Duque") > 0: #desafia fallido
                            condition = 0 #Es simplemente una condicion por si es necesario contraatacar o no
                            print (players[i].name+" tiene la carta Duque, desafío fallido.")
                            log.append(players[i].name+" tiene la carta Duque, desafío fallido.")
                            print (other_players[l].influence)
                            turn_card = input(other_players[l].name+" escriba la carta que quiere dar vuelta:")
                            print (other_players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(other_players[l].name+" ha perdido la carta: "+turn_card)
                            other_players[l].influence.remove(turn_card)
                            players[i].influence.remove("Duque") #se le quita la influencia al jugador
                            players[i].influence.append(influence_deck[0]) #la reemplaza con una del mazo
                            influence_deck.append("Duque") #se agrega la carta que se quitó al mazo
                            random.shuffle(influence_deck) #baraja el mazo con la nueva carta cartas
                            break
                        else: #desafio acertado
                            condition += 1
                            print (players[i].name+" no tiene la carta Duque, desafío correcto.")
                            log.append(players[i].name+" no tiene la carta Duque, desafío correcto.")
                            print (players[i].influence)
                            turn_card = input(players[i].name+" escriba la carta que quiere dar vuelta: ")     
                            print (players[i].name+" ha perdido la carta: "+turn_card)
                            log.append(players[i].name+" ha perdido la carta: "+turn_card)
                            players[i].influence.remove(turn_card) #se le quita la carta que eligió
                            turned_around_characters.append(turn_card) #la carta queda dada vuelta en una lista visible para todos                          
                            break                    
                if condition == 0:
                    print(players[i].name+" gana 3 mondeas al usar Duque")
                    Duke.Tax(i, players)
               
            if action == 5:
                for (n, _) in enumerate(other_players):
                    print (f"{n+1}: {other_players[n].name}")
                e = int(input("¿Selecciona a quien quieres Asesinar:"))                  
                print (players[i].name+" quiere asesinar a "+other_players[e-1].name)
                log.append(players[i].name+" quiere asesinar a "+other_players[e-1].name)
                for l in range(len(other_players)): #todos los jugadores eligen si desafian o no, de manera aleatoria
                    print ("\n"+other_players[l].name)
                    challenge = challenge_player()
                    condition = 0
                    if challenge == 1:
                        print (other_players[l].name+" desafía a "+players[i].name)
                        log.append(other_players[l].name+" desafía a "+players[i].name)
                        if players[i].influence.count("Asesino") > 0: #desafia fallido
                            condition += 1
                            print ("\n"+players[i].name+" tiene la carta Asesino, desafío fallido.")
                            log.append(players[i].name+" tiene la carta Asesino, desafío fallido.")
                            show_characters = show_my_characters() #si el jugador quiere ver sus cartas
                            if show_characters == 1:
                                print("\nTus cartas son:")
                                for j in other_players[l].influence:
                                    print (j)
                            turn_card = input(other_players[l].name+" escriba la carta que quiere dar vuelta: ")
                            print (other_players[l].name+" ha perdido la carta "+turn_card)
                            log.append(other_players[l].name+" ha perdido la carta "+turn_card)
                            other_players[l].influence.remove(turn_card)
                            print (players[i].name+" tiene que asesinar a "+other_players[l].name)
                            Assassin.Assassinate(i, players, log, turned_around_characters)
                            players[i].influence.remove("Asesino")
                            players[i].influence.append(influence_deck[0])
                            influence_deck.append("Asesino")
                            random.shuffle(influence_deck) #baraja el mazo con las cartas
                            break
                        else: #desafio acertado
                            condition += 1
                            print (players[i].name+" no tiene la carta Asesino, desafío correcto.")
                            log.append(players[i].name+" no tiene la carta Asesino, desafío correcto.")
                            print (players[i].influence)
                            turn_card = input(players[i].name+" escriba la carta que quiere dar vuelta: ")     
                            print (players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(players[l].name+" ha perdido la carta: "+turn_card)
                            players[l].influence.remove("Asesino")
                            turned_around_characters.append(turn_card)
                            break
                execute = 0 #condicion para asesinar si nadie contraataca                                     
                if condition == 0:   
                    print ("\nContraataques:")              
                    for l in range(len(other_players)): #todos los jugadores eligen si contraatacan o no, de manera aleatoria
                        print ("\n"+other_players[l].name)
                        show_characters = show_my_characters() #si el jugador quiere ver sus cartas
                        if show_characters == 1:
                            print("\nTus cartas son:")
                            for j in other_players[l].influence:
                                print (j)
                        counter = counter_attack_player()                      
                        if counter == 1:
                            print ("\n"+players[i].name)
                            challenge = challenge_counter()
                            if challenge == 1:
                                if other_players[l].influence.count("Condesa") > 0:
                                    print ("El asesinato fué bloqueado por la Condesa")
                                else:
                                    execute += 0
                                    print ("Se ejecuta el asesinato")
                                    Assassin.Assassinate(i, other_players, log, turned_around_characters)
                                break
                            if challenge == 2:  
                                print ("El asesinato fué bloqueado por la Condesa")
                                break
                if execute == 1:
                    Assassin.Assassinate(i, other_players, log, turned_around_characters)                 
            if action == 6:
                print (players[i].name+" utiliza Capitán")
                log.append(players[i].name+" utiliza Capitán")
                for l in range(len(other_players)): #todos los jugadores eligen si desafian o no, de manera aleatoria
                    print ("\n"+other_players[l].name)
                    challenge = challenge_player()
                    condition = 0
                    if challenge == 1:
                        print (other_players[l].name+" desafía a "+players[i].name)
                        log.append(other_players[l].name+" desafía a "+players[i].name)
                        if players[i].influence.count("Capitán") > 0: #desafia fallido
                            condition += 0
                            print ("\n"+players[i].name+" tiene la carta Capitán, desafío fallido.")
                            log.append(players[i].name+" tiene la carta Capitán, desafío fallido.")
                            print (other_players[l].influence)
                            turn_card = input(other_players[l].name+" escriba la carta que quiere dar vuelta: ")
                            print (other_players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(other_players[l].name+" ha perdido la carta: "+turn_card)
                            other_players[l].influence.remove(turn_card)
                            players[i].influence.remove("Capitán")
                            players[i].influence.append(influence_deck[0])
                            influence_deck.append("Capitán")
                            random.shuffle(influence_deck) #baraja el mazo con las cartas
                            break
                        else: #desafio acertado
                            condition += 1
                            print ("\n"+players[i].name+" no tiene la carta Capitán, desafío correcto.")
                            log.append(players[i].name+" no tiene la carta Capitán, desafío correcto.")
                            print (players[i].influence)
                            turn_card = input(players[i].name+" escriba la carta que quiere dar vuelta: ")     
                            print (players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(players[l].name+" ha perdido la carta: "+turn_card)
                            players[l].influence.remove("Capitán")
                            turned_around_characters.append(turn_card)
                            break
                if condition == 1:
                    break         
                else:
                    #aqui va la opción de contraatacar
                    pass  #pass es por mientras   
                
            if action == 7:
                print (players[i].name+" utiliza Embajador")
                log.append(players[i].name+" utiliza Embajador")
                for l in range(len(other_players)): #todos los jugadores eligen si desafian o no, de manera aleatoria
                    print ("\n"+other_players[l].name)
                    challenge = challenge_player()
                    condition = 0
                    if challenge == 1:
                        print (other_players[l].name+" desafía a "+players[i].name)
                        log.append(other_players[l].name+" desafía a "+players[i].name)
                        if players[i].influence.count("Embajador") > 0: #desafia fallido
                            condition += 0
                            print (players[i].name+" tiene la carta Embajador, desafío fallido.")
                            log.append(players[i].name+" tiene la carta Embajador, desafío fallido.")
                            print (other_players[l].influence)
                            turn_card = input(other_players[l].name+" escriba la carta que quiere dar vuelta: ")
                            print (other_players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(other_players[l].name+" ha perdido la carta: "+turn_card)
                            other_players[l].influence.remove(turn_card)
                            players[i].influence.remove("Embajador")
                            players[i].influence.append(influence_deck[0])
                            influence_deck.append("Embajador")
                            random.shuffle(influence_deck) #baraja el mazo con las cartas
                            break
                        else: #desafio acertado
                            condition += 1
                            print (players[i].name+" no tiene la carta Embajador, desafío correcto.")
                            log.append(players[i].name+" no tiene la carta Embajador, desafío correcto.")
                            print (players[i].influence)
                            turn_card = input(players[i].name+" escriba la carta que quiere dar vuelta: ")     
                            print (players[l].name+" ha perdido la carta: "+turn_card)
                            log.append(players[l].name+" ha perdido la carta: "+turn_card)                           
                            players[l].influence.remove("Embajador")
                            turned_around_characters.append(turn_card)
                            break
                if condition == 1:
                    break         
                else:
                    #aqui va la opción de contraatacar
                    pass  #pass es por mientras   
            if action == 0:
                break
                
        log.append(" ") #agrega un espacio para diferenciar los turnos
        show_log = show_log_game()
        if show_log == 1: #muestra el log de todos los turnos
            for t in range(len(log)):
                print (log[t])
        for m in range(len(players)):
            if len(players[m].influence) < 1:
                print (players[m].name+" ha sido eliminado del juego")
                log.append(players[m].name+" ha sido eliminado del juego")
                players.pop(m)
                break

        if len(players) == 1: #solo queda un jugador, termina el juego.
            print ("¡Felicidades "+players[0].name+"! ¡Has ganado!")
            break

# crear un sistema en que otros jugadores puedan desafiar [LISTO] o contraatacar


if __name__ == "__main__":
    initial_menu()
    initialize_game()