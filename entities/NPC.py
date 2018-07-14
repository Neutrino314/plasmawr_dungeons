import math, pygame, sys

class NPC:

    def __init__(self, name, xy, dialogue, start_end):

        self.name = name
        self.xy = xy
        self.pos = []
        self.dialogue = dialogue
        self.sprite = pygame.image.load("/home/euler/Desktop/plasmawr_game/Assets/npc_south.png")
        self.end_reached = False
        self.wait = 0
        self.interacting = False
        self.active_zone = []
        self.start_end = start_end

    def walk_x(self, wait):

        if self.end_reached == False:
            if self.xy[0] < self.start_end[1]:
                self.xy[0] += 2
            elif self.xy[0] == self.start_end[1] and self.wait == wait:
                self.end_reached = True
                self.wait = 0
            elif self.xy[0] == self.start_end[1] and self.wait != wait:
                self.wait += 1
        elif self.end_reached == True:
            if self.xy[0] > self.start_end[0]:
                self.xy[0] -= 2
            elif self.xy[0] == self.start_end[0] and self.wait == wait:
                self.end_reached = False
                self.wait = 0
            elif self.xy[0] == self.start_end[0] and self.wait != wait:
                self.wait += 1

        return self.xy

    def npc_pos(self):
        self.pos = [math.floor(self.xy[0] / 64), math.floor(self.xy[1] / 64)]

        self.active_zone = [[self.pos[0], self.pos[1]],
        [self.pos[0] + 1, self.pos[1]],
        [self.pos[0] - 1, self.pos[1]],
        [self.pos[0] + 1, self.pos[1] + 1],
        [self.pos[0] + 1, self.pos[1] - 1],
        [self.pos[0] - 1, self.pos[1] + 1],
        [self.pos[0] - 1, self.pos[1] - 1],
        [self.pos[0], self.pos[1] + 1],
        [self.pos[0], self.pos[1] - 1]]
        return

    def check_interacting(self, xy, key):

        if [math.floor(xy[0]), math.floor(xy[1])] in self.active_zone:
            if key == pygame.K_SPACE:
                self.interacting = True
                return
            else:
                return
        return
