# -*- coding: utf-8 -*-
"""
"""
from main import *

class Character:
    def __init__(self, name):
        self.name = name
    
    def income(nplayer):
        # nplayer = numero del Player en la lista players
        players[nplayer].coins += 1
        return
    
    def foreign_aid(nplayer, name_last_influence):
        # evito hacer una fx de bloqueo en Duke
        if name_last_influence != "Duke":
            players[nplayer].coins += 2
            return
        
    def coup():
        j = int(input("\nIngresa el número del jugador al cual le aplicarás el golpe "))
        players[j-1].coins -= 7
        return
    
class Duke(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Tax():
        

class Captain(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Steal():

class Assassin(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Assassinate():
        

class Ambassador(Character):
    def __init__(self, name):
        Character.__init__(self, name)
    
    def Exchange():
        

class contessa(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        
    def 