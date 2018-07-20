import pygame, sys, math

class Consumable:

    def __init__(self, description, image, name, type):

        self.descrition = descrition
        self.image = image
        self.name = names
        self.type = type

    def resize(self, dimensions):
        pass

class health_potion(Consumable):

    def use(self, player):

        if self.type == "minor":
            player.health += 3
        elif self.type == "major":
            player.health += 6

        return
