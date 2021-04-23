# -*- coding: utf-8 -*-
"""
"""
from main import *
from numpy import random

class Character:
    def __init__(self, name):
        self.name = name
    
    def income(nplayer):
        # nplayer = numero del Player en la lista players
        players[nplayer].coins += 1
        return
    
    def foreign_aid(nplayer):
        players[nplayer].coins += 2
        return
        
    def coup(nplayer):
        players[nplayer].coins -= 7
        j = int(input("\nIngresa el número del jugador al cual le aplicarás el golpe "))
        players[j-1].influence.pop(random.randint(0,1))
        return
    
class Duke(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Tax(nplayer):
        players[nplayer].coins += 3
        return
    
    def Blocks_foreign_aid(nplayer):
        players[nplayer].coins -= 2
        return
        
class Captain(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Steal():
        j = int(input("\nIngresa el número del jugador al cual extorsionarás "))
        if players[j-1].coins == 1:
            players[j-1].coins -= 1
            return
        elif players[j-1].coins > 1:
            players[j-1].coins -= 2
            return
        else:
            return

class Assassin(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Assassinate(nplayer):
        players[nplayer].coins -= 3
        j = int(input("\nIngresa el número del jugador al cual le quitarás una influencia "))
        players[j-1].influence.pop(random.randint(0,1))
        return
        
class Ambassador(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Exchange():
        
        

class contessa(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        
    def 