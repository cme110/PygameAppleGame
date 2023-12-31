'''The module containing all the sprites used in the main module.

All classes have these attributes:
    surf (pygame.surface.Surface): The image representing the sprite
    rect (pygame.rect.Rect): Position of the sprite when game begins
Apple, GoldenApple and EatenApple classes have this additional attribute:
    speed (int): Falling speed of the apple sprite

All classes have this method:
    __init__():
        Initialises the class by assigning attributes
Player, Apple, GoldenApple and EatenApple classes have this additional method:
    update():
        Moves the position of the sprite on the screen
'''

import pygame
import random
from apple_game_constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        image = pygame.image.load('Images and Sounds/basket.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (90, 50))
        self.surf.set_colorkey(BLACK, pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH/2)-(75/2), SCREEN_HEIGHT-15)
            )

    def update(self, pressed_keys):
        '''Moves sprite's position based on what keys are pressed

        Args:
            pressed_keys (pygame.key.ScancodeWrapper): Keys being pressed by the
            player
        '''
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-8,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(8,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        image = pygame.image.load('Images and Sounds/apple.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (30, 35))
        self.surf.set_colorkey(BLACK, pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(15, SCREEN_WIDTH-15), -10)
            )
        self.speed = random.randint(5, 6)

    def update(self):
        self.rect.move_ip(0, self.speed)

class GoldenApple(Apple):
    def __init__(self):
        super(GoldenApple, self).__init__()
        image = pygame.image.load('Images and Sounds/golden_apple.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (30, 35))
        self.surf.set_colorkey(BLACK, pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(15, SCREEN_WIDTH-15), -10)
            )
        self.speed = random.randint(7, 8)

class EatenApple(Apple):
    def __init__(self):
        super(EatenApple, self).__init__()
        image = pygame.image.load('Images and Sounds/eaten_apple.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (30, 35))
        self.surf.set_colorkey(BLACK, pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(15, SCREEN_WIDTH-15), -10)
            )
        self.speed = random.randint(5, 6)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        image = pygame.image.load('Images and Sounds/background.jpg').convert()
        self.surf = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = 0, 0

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super(Tree, self).__init__()
        image = pygame.image.load('Images and Sounds/tree.png').convert_alpha()
        self.surf = pygame.transform.scale(image, (700, 960))
        self.surf.set_colorkey(BLACK, pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
