# -*- coding: utf-8 -*-
"""
"""
from numpy import random

class Character:
    def __init__(self, name):
        self.name = name
    
    def income(self, all_players):
        # all_players = numero del Player en la lista players
        all_players[int(self)].coins += 1
        
    
    def foreign_aid(self, all_players):
        all_players[int(self)].coins += 2
        
        
    def coup(self, all_players, log, turned_around_characters):
        all_players[int(self)].coins -= 7
        for (k, _) in enumerate(all_players):
            print(f"{k+1}: {all_players[k].name}")
        j = int(input("\nIngresa el número del jugador al cual le aplicarás el golpe "))
        print (all_players[j-1].name+" le quedan "+str(len(all_players[j-1].influence))+" cartas.")
        z = int(input("\nIngresa el número de la carta que le quitaras a "+all_players[j-1].name+", 0 o 1"))
        log.append((all_players[int(self)].name+" realizó un golpe a "+all_players[j-1].name+
                    "\n"+all_players[j-1].name+" da vuelta la carta "+all_players[j-1].influence[z]))
        print (all_players[int(self)].name+" realizó un golpe a "+all_players[j-1].name+
                    "\n"+all_players[j-1].name+" da vuelta la carta "+all_players[j-1].influence[z])
        turned_around_characters.append(all_players[j-1].influence[z])
        all_players[j-1].influence.pop(z)
            
class Duke(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Tax(self, all_players):
        all_players[int(self)].coins += 3
        
    
    def Blocks_foreign_aid(self, all_players):
        all_players[int(self)].coins -= 2
        return
        
class Captain(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Steal(self, all_players):
        j = int(input("\nIngresa el número del jugador al cual extorsionarás "))
        if all_players[j-1].coins == 1:
            all_players[j-1].coins -= 1
            return
        elif all_players[j-1].coins > 1:
            all_players[j-1].coins -= 2
            return

class Assassin(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Assassinate(self, all_players):
        all_players[int(self)].coins -= 3
        j = int(input("\nIngresa el número del jugador al cual le quitarás una influencia "))
        all_players[j-1].influence.pop(random.randint(0,1))
        return
        
class Ambassador(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Exchange(self, all_players, influence_deck):
        print("\nTus cartas son:")
        for j in all_players[int(self)].influence:
            print (j)
        a = input("\nIngresa la posición de la 1era que quiere sacar (si no un ´no´): ")
        a2 = input("\nIngresa la posición de la 2da que quieres sacar (si no un ´no´): ") 
        if a != "no":
            all_players[int(self)].influence.pop(a)
            all_players[int(self)].influence.append(influence_deck[0])
        if a2 != "no":
            all_players[int(self)].influence.pop(a2)
            all_players[int(self)].influence.append(influence_deck[0])
        return
        
        