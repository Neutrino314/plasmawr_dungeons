import pygame, sys, math
from scripts.globals import *
from scripts.map_engine import *
from scripts.textures import *
from scripts.UltraColor import *
from entities.player import *

pygame.init()

player1 = player("Alex")
player.pos_calc(player1, [Globals.camera_x, Globals.camera_y])

width, height = 800, 600
window = pygame.display.set_mode((width, height), pygame.HWSURFACE)
pygame.display.set_caption("The Dungeons of Plasmawr")

tile_data = map_engine.load_map("/home/euler/Desktop/plasmawr_game/maps/blank.txt")

clock = pygame.time.Clock()

running = True

while running:

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

        if event.type == pygame.KEYUP:
            Globals.camera_move = 0

    if not player1.pos[1] < 0.125:
        if Globals.camera_move == 1:
            Globals.camera_y += 8
    if not player1.pos[1] > 98.875:
        if Globals.camera_move == 2:
            Globals.camera_y -= 8
    if not player1.pos[0] > 98.875:
        if Globals.camera_move == 3:
            Globals.camera_x -= 8
    if not player1.pos[0] < 0.125:
        if Globals.camera_move == 4:
            Globals.camera_x += 8

    player.pos_calc(player1, [Globals.camera_x, Globals.camera_y])

    window.fill(Color.Black)
    for tile in tile_data:
        window.blit(Tiles.texture_tags[tile[0]], (tile[1] + Globals.camera_x, tile[2] + Globals.camera_y))
    player.blit_player(player1, window)


    pygame.display.update()
    clock.tick(30)
    print(player1.pos)

pygame.quit()
sys.exit()
