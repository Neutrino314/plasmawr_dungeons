import pygame, math

class player:

    def __init__(self, name):
        self.name = name
        self.xy = [384, 256]
        self.sprite = pygame.image.load("/home/euler/Desktop/plasmawr_game/Assets/blank_south.png")
        self.pos = []


    def blit_player(self, surface):
        surface.blit(self.sprite, (self.xy[0], self.xy[1]))
        return

    def pos_calc(self, camera_xy):
        self.pos = [(self.xy[0] - camera_xy[0]) / 64, (self.xy[1] - camera_xy[1]) / 64]
        return
