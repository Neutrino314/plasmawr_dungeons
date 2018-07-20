import math, pygame, sys

class NPC:

    def __init__(self, name, xy, dialogue, start_end):

        self.name = name
        self.xy = xy
        self.pos = []
        self.dialogue = dialogue
        self.sprite = pygame.image.load("/home/euler/Desktop/plasmawr_game/Assets/NPC/npc_south.png")
        self.end_reached = False
        self.wait = 0
        self.interacting = False
        self.active_zone = []
        self.start_end = start_end
        self.text_counter = 0

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
                if self.interacting != True:
                    self.interacting = True
                    return
                elif self.interacting == True:
                    self.text_counter += 1
                    return
            else:
                return

    def dialogue(self, dimensions):
        global lines

        if self.text_counter > len(self.dialogue) - 1:
            self.interacting = False
            self.text_counter = 0
            return

        else:
            spritesheet = pygame.image.load("/home/euler/Desktop/plasmawr_game/Assets/dialogue/dialogue_menu.png")
            spritesheet = pygame.transform.scale(spritesheet, (192, 192))
            sprite_dict = {"top_left" : spritesheet.subsurface((0, 0, 64, 64)),
            "left" : spritesheet.subsurface((0, 64, 64, 64)),
            "bottom_left" : spritesheet.subsurface((0, 128, 64, 64)),
            "bottom" : spritesheet.subsurface((64, 128, 64, 64)),
            "bottom_right" : spritesheet.subsurface((128, 128, 64, 64)),
            "right" : spritesheet.subsurface((128, 64, 64, 64)),
            "top_right" : spritesheet.subsurface((128, 0, 64, 64)),
            "top" : spritesheet.subsurface((64, 0, 64, 64)),
            "centre" : spritesheet.subsurface((64, 64, 64, 64))}
            dimensions = [11, 3]

            surface = pygame.Surface((dimensions[0] * 64, dimensions[1] * 64), pygame.HWSURFACE|pygame.SRCALPHA)

            for row in range(0, int(dimensions[1])):
                for column in range(0, int(dimensions[0])):

                    if row == 0:
                        if column == 0:
                            surface.blit(sprite_dict["top_left"], (0, 0))
                        elif column == dimensions[0] - 1:
                            surface.blit(sprite_dict["top_right"], (column * 64, row))
                        else:
                            surface.blit(sprite_dict["top"], (column * 64, row))
                    elif row == dimensions[1] - 1:
                        if column == 0:
                            surface.blit(sprite_dict["bottom_left"], (0, row * 64))
                        elif column == dimensions[0] - 1:
                            surface.blit(sprite_dict["bottom_right"], (column * 64, row * 64))
                        else:
                            surface.blit(sprite_dict["bottom"], (column * 64, row * 64))
                    elif column == 0:
                        surface.blit(sprite_dict["left"], (0, row * 64))
                    elif column == dimensions[0]- 1:
                        surface.blit(sprite_dict["right"], (column * 64, row * 64))
                    else:
                        surface.blit(sprite_dict["centre"], (column * 64, row * 64))

            font = pygame.font.Font("/home/euler/Desktop/plasmawr_game/Assets/dialogue/PressStart2P.ttf", 13)
            cur_line = ""
            text_list = self.dialogue[self.text_counter]
            text_list = text_list.split(" ")
            lines = []
            y = 25

            for i in range(0, len(text_list)):

                if font.size(cur_line + text_list[i] + " ")[0] > dimensions[0] * 64:
                    lines.append(cur_line)
                    cur_line = text_list[i] + " "
                elif i == len(text_list) - 1:
                    cur_line = cur_line + text_list[i] + " "
                    lines.append(cur_line)
                else:
                    cur_line = cur_line + text_list[i] + " "

            for line in lines:
                text = font.render(line, 0, (0, 0, 0))
                surface.blit(text, (64, 32))
                y += 25


            return surface
