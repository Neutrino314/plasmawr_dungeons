import pygame
import sys
import math
from scripts.textures import *
from scripts.globals import *
from scripts.UltraColor import *
from scripts.map_engine import *

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height), pygame.HWSURFACE)
pygame.display.set_caption("Map editor")

mouse_x, mouse_y = 0, 0
tile_data = map_engine.load_map("/home/euler/Desktop/plasmawr_game/maps/blank.txt")

def save_map(tiles_data):
    name = str(input("Choose a file name: "))
    map_data = ""
    file = open(("/home/euler/Desktop/plasmawr_game/maps/" + name + ".txt"), "w")
    for tile in tiles_data:
        map_data += tile[0] + "," + str(tile[1]) + "," + str(tile[2]) + "|"
    file.write(map_data)

brush = "2"
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                Globals.camera_move = 1
            if event.key == pygame.K_s:
                Globals.camera_move = 2
            if event.key == pygame.K_d:
                Globals.camera_move = 3
            if event.key == pygame.K_a:
                Globals.camera_move = 4
            if event.key == pygame.K_r:
                brush = "r"
            if event.key == pygame.K_1:
                brush = str(input("Choose a brush: "))
            if event.key == pygame.K_2:
                save_map(tile_data)

        if event.type == pygame.KEYUP:
            Globals.camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tile_data:
                if mouse_pos[0] - Globals.camera_x == tile[1] and mouse_pos[1] - Globals.camera_y == tile[2]:
                    if not brush == tile[0]:
                        tile_data[tile_data.index(tile)][0] = brush
                    else:
                        print("A tile is already placed there")
                    if brush == "r":
                        tile_data[tile_data.index(tile)][0] = "r"

    if Globals.camera_move == 1:
        Globals.camera_y += Tiles.size
    if Globals.camera_move == 2:
        Globals.camera_y -= Tiles.size
    if Globals.camera_move == 3:
        Globals.camera_x -= Tiles.size
    if Globals.camera_move == 4:
        Globals.camera_x += Tiles.size
    mouse_pos = [math.floor(mouse_x / Tiles.size) * 64, math.floor(mouse_y / Tiles.size) * 64]

    window.fill(Color.Blue)

    for tile in tile_data:
        if not tile[0] == "r":
            window.blit(Tiles.texture_tags[tile[0]], (tile[1] + Globals.camera_x, tile[2] + Globals.camera_y))
        else:
            continue

    pygame.draw.rect(window, Color.DodgerBlue, (mouse_pos[0], mouse_pos[1], Tiles.size, Tiles.size))

    pygame.display.update()
    clock.tick(30)


pygame.quit()
sys.exit
