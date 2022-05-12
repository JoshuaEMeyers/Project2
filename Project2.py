import random
import pygame
import time

pygame.init()

black = (0, 0, 0)
gray = (119, 118, 110)
red = (255, 0, 0)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Galactic Debris")
clock = pygame.time.Clock()
shipimg = pygame.image.load('FreeShip.png')
shipwidth = 84
shipheight = 61
backgroundpic = pygame.image.load('background.jpg')

def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed " + str(passed), True, gray)
    scored = font.render("Score " + str(score), True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(scored, (0, 30))

def text_objects(text, font):
    textsurface = font.render(text, True, gray)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("You Crashed")


def enemy(obs_start_x, obs_start_y, obs):
    if obs == 0:
        asteroidpick = pygame.image.load('asteroid.png')
    elif obs == 1:
        asteroidpick = pygame.image.load('asteroid1.png')
    elif obs == 2:
        asteroidpick = pygame.image.load('asteroid2.png')
    else:
        asteroidpick = pygame.image.load('asteroid3.png')
    gamedisplays.blit(asteroidpick, (obs_start_x, obs_start_y))


def background():
    gamedisplays.blit(backgroundpic, (0, 0))


def ship(x, y):
    gamedisplays.blit(shipimg, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.9)
    x_change = 0
    y_change = 0
    obstacle_speed = 9
    obs = 0
    obs_start_y = -750
    obs_width = 130
    obs_height = 130
    obs_start_x = random.randrange(0, (display_width - obs_width))
    passed = 0
    level = 0
    score = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x > 800 - shipwidth:
                    x_change = 0
                else:
                    x_change = 5
            if event.key == pygame.K_LEFT:
                if x < 0:
                    x_change = 0
                else:
                    x_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y < 0:
                    y_change = 0
                else:
                    y_change = -5
            if event.key == pygame.K_DOWN:
                if y > 600 - shipheight:
                    y_change = 0
                else:
                    y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        x += x_change
        y += y_change
        gamedisplays.fill(black)
        background()
        obs_start_y -= (obstacle_speed / 4)
        enemy(obs_start_x, obs_start_y, obs)
        obs_start_y += obstacle_speed
        ship(x, y)
        score_system(passed, score)
        if obs_start_y > display_height:
            obs_start_y = 0 - obs_height
            obs_start_x = random.randrange(0, (display_width - obs_width))
            obs = random.randrange(0, 4)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level += 1
                largetext = pygame.font.Font('freesansbold.ttf', 80)
                textsurf, textrect = text_objects('LEVEL ' + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_start_y + obs_height:
            if x > obs_start_x and x < obs_start_x + obs_width or x + shipwidth > obs_start_x and x + shipwidth < obs_start_x + obs_width:
                crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
