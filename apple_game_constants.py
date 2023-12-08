'''The module containing all of the constant variables used in the main module,
plus a function for creating in game text.
'''

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

# Creates events for adding each type of apple
ADDAPPLE = pygame.USEREVENT + 1
ADDGOLDEN = pygame.USEREVENT + 2
ADDEATEN = pygame.USEREVENT + 3

# Creates event for when one second has passed
SECOND = pygame.USEREVENT + 4

# Creates clock
clock = pygame.time.Clock()

def game_text(string):
    '''Creates text used in the game and gets the width and height of the text.

    Args:
        string (str): The text that will be displayed

    Returns:
        text (pygame.surface.Surface): Text with white background
        width (int): Width of the text
        height (int): Height of the text
    '''
    text = font.render(string, True, BLACK, WHITE)
    width = text.get_width()
    height = text.get_height()
    return text, width, height
