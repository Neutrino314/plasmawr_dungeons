import pygame, sys, math
from scripts.globals import *
from scripts.map_engine import *
from scripts.textures import *
from scripts.UltraColor import *
from entities.player import *
from entities.NPC import *

pygame.init()

player1 = player("Alex")
player.pos_calc(player1, [Globals.camera_x, Globals.camera_y])

steffan = NPC("stwffin", [0, 0],["Have you seen link?", "We still haven't finished..."], [0, 128])
Skinner = NPC("Skinner", [256, 128], ["Do you know what I did in Nam?", "It wasn't pretty..."], [256, 512])

npc_list = [steffan, Skinner]

for npc in npc_list:
    NPC.npc_pos(npc)

width, height = 800, 600
window = pygame.display.set_mode((width, height), pygame.HWSURFACE)
pygame.display.set_caption("The Dungeons of Plasmawr")

tile_data = map_engine.load_map("/home/euler/Desktop/plasmawr_game/maps/blank.txt")
Tiles.blocked = map_engine.blocked(tile_data, Tiles.blocked_types, Tiles.blocked)

clock = pygame.time.Clock()

running = True

while running:

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

                for npc in npc_list:
                    NPC.check_interacting(npc, player1.pos, key_pressed)
                    if npc.interacting == True:
                        Globals.scene = npc.name
                    else:
                        continue


            if event.type == pygame.KEYUP:
                Globals.camera_move = 0

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
            window.blit(Tiles.texture_tags[tile[0]], (tile[1] + Globals.camera_x, tile[2] + Globals.camera_y))
        for npc in npc_list:
            window.blit(npc.sprite, (npc.xy[0] + Globals.camera_x, npc.xy[1] + Globals.camera_y))
        player.blit_player(player1, window)

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
                window.blit(dialogue, (20, 400))
            else:
                Globals.scene = "world"


    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
