import pygame
pygame.init()

# Width and height of the screen
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 600

# Creates screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sets screen name and icon
pygame.display.set_caption('Apple Game')
icon = pygame.image.load('Images/apple.png')
pygame.display.set_icon(icon)

# Colours white and black
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font and font size of text
font = pygame.font.SysFont('Arial', 40)

# Creates event for adding an apple
ADDAPPLE = pygame.USEREVENT + 1

# Creates event for when one second has passed
SECOND = pygame.USEREVENT + 2

# Creates clock
clock = pygame.time.Clock()

# Creates text used in the game
def game_text(string):
    text = font.render(string, True, BLACK, WHITE)
    width = text.get_width()
    height = text.get_height()
    return text, width, height
