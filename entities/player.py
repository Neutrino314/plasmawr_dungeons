import pygame, math

class player:

    def __init__(self, name):
        self.name = name
        self.xy = [384, 256]
        self.sprite = pygame.image.load("/home/euler/Desktop/plasmawr_game/Assets/blank_south.png")
        self.pos = []
        self.x_pos_colliding = False
        self.x_neg_colliding = False
        self.y_neg_colliding = False
        self.y_pos_colliding = False


    def blit_player(self, surface):
        surface.blit(self.sprite, (self.xy[0], self.xy[1]))
        return

    def pos_calc(self, camera_xy):
        self.pos = [(self.xy[0] - camera_xy[0]) / 64, (self.xy[1] - camera_xy[1]) / 64]
        return

    def edge_collide(self, boundaries):
        if self.pos[0] < boundaries[0] + 0.125:
            self.x_pos_colliding = True
        elif self.pos[0] > boundaries[1] - 0.125:
            self.x_neg_colliding = True
        elif self.pos[1] < boundaries[2] + 0.125:
            self.y_neg_colliding = True
        elif self.pos[1] > boundaries[3] - 0.125:
            self.y_pos_colliding = True
        else:
            self.x_neg_colliding = False
            self.y_neg_colliding = False
            self.x_pos_colliding = False
            self.y_pos_colliding = False

        return

    def barrier_collide(self, blocked):

        for i in range(0, len(blocked)):
            if self.pos[0] < blocked[i][0] + 1.125 and (self.pos[1] < blocked[i][1] + 1 and self.pos[1] > blocked[i][1] - 0.875) and self.pos[0] > blocked[i][0] - 1.125:
                self.x_pos_colliding = True
            if self.pos[0] > blocked[i][0] - 1.125 and (self.pos[1] < blocked[i][1] + 1 and self.pos[1] > blocked[i][1] - 0.875) and self.pos[0] < blocked[i][0] + 1.125:
                self.x_neg_colliding = True
            if self.pos[1] < blocked[i][1] + 1.125 and (self.pos[0] < blocked[i][0] + 1 and self.pos[0] > blocked[i][0] - 0.875) and self.pos[1] > blocked[i][1] - 1.125:
                self.y_neg_colliding = True
            if self.pos[1] > blocked[i][1] - 1.125 and (self.pos[0] < blocked[i][0] + 1 and self.pos[0] > blocked[i][0] - 0.875) and self.pos[1] < blocked[i][1] + 1.125:
                self.y_pos_colliding = True

        return
