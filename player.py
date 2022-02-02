import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        # THREE THINGS U ALWAYS NEED IN SPRITES
        self.image = pygame.image.load('assets/Red-Ghost-Left.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        # Up and Down Controls
        if keys[pygame.K_w]:
            self.direction.y -= 1
        elif keys [pygame.K_s]:
            self.direction.y += 1
        else:
            self.direction.y = 0

        # Left and Right Controls
        if keys[pygame.K_a]:
            self.direction.x -= 1
        elif keys [pygame.K_d]:
            self.direction.x += 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()


        self.rect.x += self.direction.x * speed
        # self.collision('horizontal')
        self.rect.y += self.direction.y * speed

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # Moving Right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # Moving Left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # Moving Down
                        self.rect.Bottom = self.rect.top
                    if self.direction.y < 0: # Moving Up
                        self.rect.top = self.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)
