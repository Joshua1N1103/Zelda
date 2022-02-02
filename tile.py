import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # TWO THINGS U ALWAYS NEED IN SPRITES
        self.image = pygame.image.load('assets/Grass-Block.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        # TWO THINGS U ALWAYS NEED IN SPRITES