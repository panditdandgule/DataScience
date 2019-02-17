#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 07:38:41 2019

@author: pandit
"""

#classes and objects

#simple class

class Fish:
    def swim(self):
        print("Fish is swimming")
    def eat(self):
        print("Fish is eating")
        
fish=Fish()
fish.swim()
fish.eat()

#Overriding Constructor
class Game:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(self.name,"has started")
    def stop(self):
        print(self.name,"has stopped")
        
game=Game("Counter Strike")
game.start()
game.stop()