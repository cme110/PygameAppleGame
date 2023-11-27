import pygame
from apple_game_sprites import *

pygame.init()

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = Background()
tree = Tree()

ADDAPPLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDAPPLE, 250)

player = Player()
apples = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

caught_apples = 0
missed_apples = 0
font = pygame.font.SysFont('Arial', 35)

clock = pygame.time.Clock()

running = True
paused = False

while running:
    if paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True

            elif event.type == ADDAPPLE:
                new_apple = Apple()
                apples.add(new_apple)
                all_sprites.add(new_apple)
                
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        apples.update()
        
        screen.fill(black)
        screen.blit(background.surf, background.rect)
        for x in [-300, 500, 250, 10, 800]:
            screen.blit(tree.surf, (x, -300))
        
        score = font.render(f'Score: {caught_apples}', True, black, white)
        missed = font.render(f'Missed: {missed_apples}', True, black, white)
        if caught_apples == 0 and missed_apples == 0:
            percentage = font.render('0%', True, black, white)
        elif missed_apples == 0:
            percentage = font.render('100%', True, black, white)
        else:
            percent = (caught_apples/missed_apples) * 100
            percentage = font.render(f'{percent:.0f}%', True, black, white)
        screen.blit(score, (0,0))
        screen.blit(missed, (0, 50))
        screen.blit(percentage, (0, 100))
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        for apple in apples:
            if apple.rect.bottom >= SCREEN_HEIGHT+10:
                apple.kill()
                missed_apples += 1
        if pygame.sprite.spritecollide(player, apples, dokill=True):
            caught_apples += 1
            
        pygame.display.flip()
        clock.tick(70)

pygame.quit()
