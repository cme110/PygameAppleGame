'''The main module for running the apple game.
'''

import sys
import pygame
import random
from apple_game_constants import *
from apple_game_sprites import *
pygame.init()

# Assigning sprites and sprite groups
background = Background()
tree = Tree()
player = Player()
apples = pygame.sprite.Group()
golden_apples = pygame.sprite.Group()
eaten_apples = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Assigning initial scores to zero
caught_apples = 0
missed_apples = 0
h_score = 0

# Assigning times for each type of apple in each difficulty setting
EASY = {'apple time': 350, 'golden time': random.randint(5000, 10000), 'eaten time': 1000}
NORMAL = {'apple time': 250, 'golden time': random.randint(8000, 13000), 'eaten time': 900}
HARD = {'apple time': 150, 'golden time': random.randint(11000, 16000), 'eaten time': 800}

def game_loop(difficulty):
    '''The main game loop.

    Args:
        difficulty (dict): A dictionary of times for each type of apple to appear in the game

    Returns:
        play_again (bool): Whether the player wants to play the game again with the same
        difficulty
    '''
    running = True
    paused = False
    game_over = False
    play_again = False
    global caught_apples
    global missed_apples
    time = 60
    while running:
        caught, caught_width, caught_height = game_text(f'Caught: {caught_apples}')
        missed, missed_width, missed_height = game_text(f'Missed: {missed_apples}')
        time_left, time_width, time_height = game_text(f'Time left: {time}')
        pause, pause_width, pause_height = game_text('Press Esc to pause')
        
        if caught_apples <= 0 or caught_apples+missed_apples == 0:
            percent = 0
        else:
            percent = (caught_apples/(caught_apples + missed_apples)) * 100
        percentage, percentage_width, _ = game_text(f'Score: {percent:.0f}%')

        if h_score == 0:
            highscore, highscore_width, highscore_height = game_text('High Score: N/A')                
        else:
            highscore, highscore_width, highscore_height = game_text(f'High Score: {h_score:.0f}%')

        if difficulty == EASY:
            diff, diff_width, diff_height = game_text('Difficulty: Easy')
        elif difficulty == NORMAL:
            diff, diff_width, diff_height = game_text('Difficulty: Normal')
        elif difficulty == HARD:
            diff, diff_width, diff_height = game_text('Difficulty: Hard')
            
        if paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                        pygame.time.set_timer(ADDAPPLE, difficulty['apple time'])
                        pygame.time.set_timer(ADDGOLDEN, difficulty['golden time'])
                        pygame.time.set_timer(ADDEATEN, difficulty['eaten time'])
                        pygame.time.set_timer(SECOND, 1000)
                        
            pause, pause_width, pause_height = game_text('Press Esc to continue')
            screen.blit(pause, ((SCREEN_WIDTH/2) - (pause_width/2), (SCREEN_HEIGHT/2) - (pause_height/2)))
            pygame.display.flip()

        elif game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        play_again = True
                        running = False
                        
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        
            pygame.time.set_timer(ADDAPPLE, 0)
            pygame.time.set_timer(ADDGOLDEN, 0)
            pygame.time.set_timer(ADDEATEN, 0)
            pygame.time.set_timer(SECOND, 0)

            text1 = "Time's Up!"
            text2 = f'You caught {caught_apples} out of {caught_apples+missed_apples} apples'
            text3 = f'Your score is {percent:.0f}%'
            text4 = 'Press Enter to play again. Press Esc to change difficulty'
            timeup, timeup_width, timeup_height = game_text(text1)
            result, result_width, result_height = game_text(text2)
            score, score_width, score_height = game_text(text3)
            again, again_width, again_height = game_text(text4)
            screen.blit(timeup, ((SCREEN_WIDTH/2) - (timeup_width/2), (SCREEN_HEIGHT/2) - (result_height/2) - result_height))
            screen.blit(result, ((SCREEN_WIDTH/2) - (result_width/2), (SCREEN_HEIGHT/2) - (result_height/2)))
            screen.blit(score, ((SCREEN_WIDTH/2) - (score_width/2), (SCREEN_HEIGHT/2) - (result_height/2) + result_height))
            screen.blit(again, ((SCREEN_WIDTH/2) - (again_width/2), (SCREEN_HEIGHT/2) - (result_height/2) + result_height*3))
            pygame.display.flip()
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                        pygame.time.set_timer(ADDAPPLE, 0)
                        pygame.time.set_timer(ADDGOLDEN, 0)
                        pygame.time.set_timer(ADDEATEN, 0)
                        pygame.time.set_timer(SECOND, 0)

                elif event.type == ADDAPPLE:
                    new_apple = Apple()
                    apples.add(new_apple)
                    all_sprites.add(new_apple)

                elif event.type == ADDGOLDEN:
                    new_apple = GoldenApple()
                    golden_apples.add(new_apple)
                    all_sprites.add(new_apple)
                    pygame.time.set_timer(ADDGOLDEN, difficulty['golden time'])

                elif event.type == ADDEATEN:
                    new_apple = EatenApple()
                    eaten_apples.add(new_apple)
                    all_sprites.add(new_apple)
                    
                elif event.type == SECOND:
                    time -= 1

            if time <= 0:
                for apple in apples:
                    apple.kill()
                for apple in golden_apples:
                    apple.kill()
                for apple in eaten_apples:
                    apple.kill()
                game_over = True
                    
            screen.fill(BLACK)
            screen.blit(background.surf, background.rect)
            for x in [-300, 500, 250, 10, 800]:
                screen.blit(tree.surf, (x, -300))

            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)
            apples.update()
            golden_apples.update()
            eaten_apples.update()

            if not game_over:    
                screen.blit(caught, (0, 0))
                screen.blit(missed, (caught_width+5, 0))
                screen.blit(percentage, (caught_width+missed_width+10, 0))
                screen.blit(highscore, (caught_width+missed_width+percentage_width+15, 0))
                screen.blit(diff, (0, caught_height+5))
                screen.blit(time_left, (diff_width+5, caught_height+5))

            if not game_over and not paused:
                screen.blit(pause, (SCREEN_WIDTH-pause_width, 0))
            
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            for apple in apples:
                if apple.rect.bottom >= SCREEN_HEIGHT+10:
                    apple.kill()
                    missed_apples += 1
            for apple in golden_apples:
                if apple.rect.bottom >= SCREEN_HEIGHT+10:
                    apple.kill()
                    missed_apples += 3
            for apple in eaten_apples:
                if apple.rect.bottom >= SCREEN_HEIGHT+10:
                    apple.kill()
                    missed_apples -= 1
                
            if pygame.sprite.spritecollide(player, apples, dokill=True):
                caught_apples += 1
            if pygame.sprite.spritecollide(player, golden_apples, dokill=True):
                caught_apples += 3
            if pygame.sprite.spritecollide(player, eaten_apples, dokill=True):
                caught_apples -= 1
                  
            pygame.display.flip()
            clock.tick(70)
            
    return play_again

def main():
    '''Starts background sounds, displays start menu until user presses Enter, displays difficulty menu until
    user clicks on a setting, runs game loop with that difficulty setting when Enter is pressed and continues
    running game loop while play_again is True. If play_again is False, program shows difficulty menu again,
    and user picks new difficulty. Program stops when user exits the Pygame window.
    '''
    
    pygame.mixer.init()
    pygame.mixer.music.load('Images and Sounds/bird_sounds.mp3')
    pygame.mixer.music.play(loops=-1)

    next_menu = False
    while not next_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    next_menu = True
                    
        text1 = 'Catch as many apples as you can in your basket'
        text2 = 'Use the left and right keys to control the basket'
        text3 = '1 golden apple = 3 normal apples'
        text4 = '1 eaten apple = -1 normal apples'
        text5 = 'Press Enter to start'
        aim, aim_width, aim_height = game_text(text1)
        controls, controls_width, controls_height = game_text(text2)
        golden, golden_width, golden_height = game_text(text3)
        eaten, eaten_width, eaten_height = game_text(text4)
        start, start_width, start_height = game_text(text5)

        screen.fill(BLACK)
        screen.blit(background.surf, background.rect)
        for x in [-300, 500, 250, 10, 800]:
            screen.blit(tree.surf, (x, -300))

        screen.blit(aim, ((SCREEN_WIDTH/2) - (aim_width/2), (SCREEN_HEIGHT/2) - (controls_height/2) - controls_height*2))    
        screen.blit(controls, ((SCREEN_WIDTH/2) - (controls_width/2), (SCREEN_HEIGHT/2) - (controls_height/2) - controls_height))
        screen.blit(golden, ((SCREEN_WIDTH/2) - (golden_width/2), (SCREEN_HEIGHT/2) - (controls_height/2)))
        screen.blit(eaten, ((SCREEN_WIDTH/2) - (eaten_width/2), (SCREEN_HEIGHT/2) - (controls_height/2) + controls_height))
        screen.blit(start, ((SCREEN_WIDTH/2) - (start_width/2), (SCREEN_HEIGHT/2) - (controls_height/2) + controls_height*3))
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_x <= mouse[0] <= easy_x + easy_width and easy_y <= mouse[1] <= easy_y + easy_height:
                    difficulty = EASY
                elif normal_x <= mouse[0] <= normal_x + normal_width and normal_y <= mouse[1] <= normal_y + normal_height:
                    difficulty = NORMAL
                elif hard_x <= mouse[0] <= hard_x + hard_width and hard_y <= mouse[1] <= hard_y + hard_height:
                    difficulty = HARD
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()
                        pygame.quit()
                        sys.exit()

                pygame.time.set_timer(ADDAPPLE, difficulty['apple time'])
                pygame.time.set_timer(ADDGOLDEN, difficulty['golden time'])
                pygame.time.set_timer(ADDEATEN, difficulty['eaten time'])
                pygame.time.set_timer(SECOND, 1000)
                play_again = game_loop(difficulty)
                while play_again:
                    player = Player()
                    apples = pygame.sprite.Group()
                    golden_apples = pygame.sprite.Group()
                    all_sprites = pygame.sprite.Group()
                    all_sprites.add(player)

                    global caught_apples
                    global missed_apples
                    global h_score
                    percent = (caught_apples/(caught_apples + missed_apples)) * 100
                    if percent > h_score:
                        h_score = percent
                    caught_apples = 0
                    missed_apples = 0
                        
                    pygame.time.set_timer(ADDAPPLE, difficulty['apple time'])
                    pygame.time.set_timer(ADDGOLDEN, difficulty['golden time'])
                    pygame.time.set_timer(ADDEATEN, difficulty['eaten time'])
                    pygame.time.set_timer(SECOND, 1000)
                    play_again = game_loop(difficulty)
                    
                caught_apples = 0
                missed_apples = 0
                h_score = 0
                    
        mouse = pygame.mouse.get_pos()
                
        easy, easy_width, easy_height = game_text('Easy')
        normal, normal_width, normal_height = game_text('Normal')
        hard, hard_width, hard_height = game_text('Hard')
        choice, choice_width, choice_height = game_text('Click on a difficulty setting to start the game')
        screen.fill(BLACK)
        screen.blit(background.surf, background.rect)
        for x in [-300, 500, 250, 10, 800]:
            screen.blit(tree.surf, (x, -300))
        screen.blit(easy, ((SCREEN_WIDTH/2) - (normal_width/2) - easy_width*2, (SCREEN_HEIGHT/2) - (easy_height/2)))
        screen.blit(normal, ((SCREEN_WIDTH/2) - (normal_width/2), (SCREEN_HEIGHT/2) - (normal_height/2)))
        screen.blit(hard, ((SCREEN_WIDTH/2) - (normal_width/2) + normal_width+hard_width, (SCREEN_HEIGHT/2) - (hard_height/2)))
        screen.blit(choice, ((SCREEN_WIDTH/2) - (choice_width/2), (SCREEN_HEIGHT/2) - (choice_height/2) + choice_height*2))
        pygame.display.flip()

        easy_x = (SCREEN_WIDTH/2) - (normal_width/2) - easy_width*2
        easy_y = (SCREEN_HEIGHT/2) - (easy_height/2)
        normal_x = (SCREEN_WIDTH/2) - (normal_width/2)
        normal_y = (SCREEN_HEIGHT/2) - (normal_height/2)
        hard_x = (SCREEN_WIDTH/2) - (normal_width/2) + normal_width+hard_width
        hard_y = (SCREEN_HEIGHT/2) - (hard_height/2)

if __name__ == '__main__':
    main()
