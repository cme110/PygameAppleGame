import pygame
import random
from apple_game_constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        image = pygame.image.load('Images/basket.png').convert()
        self.surf = pygame.transform.scale(image, (90, 50))
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH/2)-(75/2), SCREEN_HEIGHT-15)
            )

    def update(self, pressed_keys):
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
        image = pygame.image.load('Images/apple.png').convert()
        self.surf = pygame.transform.scale(image, (30, 35))
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(0, SCREEN_WIDTH), -10)
            )
        self.speed = random.randint(5, 6)

    def update(self):
        self.rect.move_ip(0, self.speed)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        image = pygame.image.load('Images/background.jpg').convert()
        self.surf = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = 0, 0

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super(Tree, self).__init__()
        image = pygame.image.load('Images/tree.png').convert()
        self.surf = pygame.transform.scale(image, (700, 960))
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
