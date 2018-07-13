import pygame

class Tiles:

    size = 64
    blocked_types = ["3"]
    blocked = []

    def load_texture(size, file):

        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        texture = pygame.image.load(file)
        surface.blit(texture, (0, 0))

        return surface

    grass = load_texture(size, "/home/euler/Desktop/plasmawr_game/Assets/isolated_grass.png")
    concrete = load_texture(size, "/home/euler/Desktop/plasmawr_game/Assets/concrete_isolated.png")
    barrier = load_texture(size, "/home/euler/Desktop/plasmawr_game/Assets/barrier.png")

    texture_tags = {"1" : grass, "2" : concrete, "3" : barrier}
