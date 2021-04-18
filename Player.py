# -*- coding: utf-8 -*-
"""

"""

class Player:
    def __init__(self, name, influence, coins):
        self.__name = name
        self.__influence = influence
        self.__coins = coins
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def influence(self):
        return self.__influence
    
    @influence.setter
    def influence(self, value):
        self.__influence = value
    
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, value):
        self.__coins = int(value)
        