import pygame, sys, math
from scripts.globals import *
from scripts.map_engine import *
from scripts.textures import *
from scripts.UltraColor import *
from entities.player import *
from entities.NPC import *

pygame.init()

#Declaring NPC's, player, world and ither variables / functions needed in the main gameloop---------------------------------------

player1 = player("Alex", 9)
player.pos_calc(player1, [Globals.camera_x, Globals.camera_y])

steffan = NPC("stwffin", [0, 0],["Have you seen link?", "We still haven't finished..."], [0, 128])
Skinner = NPC("Skinner", [256, 128], ["Do you know what I did in Nam?", "It wasn't pretty..."], [256, 512])

npc_list = [steffan, Skinner]

for npc in npc_list:
    NPC.npc_pos(npc)

size = [800, 600]
window = pygame.display.set_mode(size, pygame.HWSURFACE|pygame.RESIZABLE|pygame.DOUBLEBUF)
pygame.display.set_caption("The Dungeons of Plasmawr")

tile_data = map_engine.load_map("/home/euler/Desktop/plasmawr_game/maps/blank.txt")
Tiles.blocked = map_engine.blocked(tile_data, Tiles.blocked_types, Tiles.blocked)
render_chunk = pygame.Rect(-64, -64, (size[0] + 128), (size[1] + 128))

def resize(play, npc_array, tile_size, dimensions, resizing):

    dimensions_list = [dimensions[0] - size[0], dimensions[1] - size[1]]

    display = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
    resizing = True
    x, y = 0, 0

    xy = [play.xy[0], play.xy[1]]

    while resizing:
        if x < (event.dict["size"][0] / 2):
            x += 64
            continue
        elif x > (event.dict["size"][0] / 2):
            x -= 64
            play.xy[0] = x
            resizing = False

        if y < (event.dict["size"][1] / 2):
            y += 64
            continue
        elif y > (event.dict["size"][1] / 2):
            y -= 64
            play.xy[1] = y
            resizing = False
            continue
    Globals.camera_x += x - xy[0]
    Globals.camera_y -= y - 64

    player.pos_calc(play, (Globals.camera_x, Globals.camera_y))

    return

clock = pygame.time.Clock()

running = True
resizing = False

#main game loop---------------------------------------------------------------------------------------------

while running:
#section of the loop that runs when exploring the world------------------------
    if Globals.scene == "world":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key_pressed = event.key
                if key_pressed == pygame.K_w:
                    Globals.camera_move = 1
                if key_pressed == pygame.K_s:
                    Globals.camera_move = 2
                if key_pressed == pygame.K_d:
                    Globals.camera_move = 3
                if key_pressed == pygame.K_a:
                    Globals.camera_move = 4
                if key_pressed == pygame.K_e:
                    Globals.scene = "backpack"
                    player1.in_backpack = True

                for npc in npc_list:
                    NPC.check_interacting(npc, player1.pos, key_pressed)
                    if npc.interacting == True:
                        Globals.scene = npc.name
                    else:
                        continue

            if event.type == pygame.KEYUP:
                Globals.camera_move = 0

            if event.type == pygame.VIDEORESIZE:
                resize(player1, npc_list, Tiles.size, [event.dict["size"][0], event.dict["size"][1]], True)
                render_chunk = pygame.Rect(-64, -64, event.dict["size"][0] + 128, event.dict["size"][1] + 128)

        player.edge_collide(player1, [0, 99, 0, 99])
        player.barrier_collide(player1, Tiles.blocked)
        for npc in npc_list:
            npc.xy = NPC.walk_x(npc, 60)

        if not player1.y_neg_colliding:
            if Globals.camera_move == 1:
                Globals.camera_y += 8
        if not player1.y_pos_colliding:
            if Globals.camera_move == 2:
                Globals.camera_y -= 8
        if not player1.x_neg_colliding:
            if Globals.camera_move == 3:
                Globals.camera_x -= 8
        if not player1.x_pos_colliding:
            if Globals.camera_move == 4:
                Globals.camera_x += 8

        player.pos_calc(player1, [Globals.camera_x, Globals.camera_y])
        for npc in npc_list:
            NPC.npc_pos(npc)

        window.fill(Color.Black)
        for tile in tile_data:
            if render_chunk.collidepoint(tile[1] + Globals.camera_x, tile[2] + Globals.camera_y) == True:
                window.blit(Tiles.texture_tags[tile[0]], (tile[1] + Globals.camera_x, tile[2] + Globals.camera_y))
            else:
                continue
        for npc in npc_list:
            if render_chunk.collidepoint(npc.xy[0] + Globals.camera_x, npc.xy[1] + Globals.camera_y) == True:
                window.blit(npc.sprite, (npc.xy[0] + Globals.camera_x, npc.xy[1] + Globals.camera_y))
            else:
                continue
        player.blit_player(player1, window)

#loop used when interacting with NPC's
    for npc in npc_list:
        if Globals.scene == npc.name:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    key_pressed = event.key
                    NPC.check_interacting(npc, player1.pos, key_pressed)

                if event.type == pygame.KEYUP:
                    pass

            dialogue = NPC.dialogue(npc, (600, 50))

            if npc.interacting == True:
                window.blit(dialogue, (((render_chunk[2] - 128) - 760) / 2, render_chunk[3] - 348))
            else:
                Globals.scene = "world"

#Backpack logic----------------------------------------------------------------
    if Globals.scene == "backpack":

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                key_pressed = event.key

                if key_pressed == pygame.K_e:
                    Globals.scene = "world"
                    player1.in_backpack = False
                if key_pressed == pygame.K_w:
                    player1.selected_item[1] -= 1
                if key_pressed == pygame.K_s:
                    player1.selected_item[1] += 1
                if key_pressed == pygame.K_d:
                    player1.selected_item[0] += 1
                if key_pressed == pygame.K_a:
                    player1.selected_item[0] -= 1

            if event.type == pygame.KEYUP:
                pass

        backpack = player.in_backpack(player1)
        window.blit(backpack, (20, 20))

#updating the display
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
