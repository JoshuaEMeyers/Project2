# Original Idea: https://www.youtube.com/c/Iknowpython *the Car Game video series
# Added features: Changed the imgs from cars to spaceships and asteroids.
#                 Made it possible to move on the y-axis as well

import random
import sys
import pygame
import time
pygame.init()
black = (0, 0, 0)
gray = (119, 118, 110)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Galactic Debris")
clock = pygame.time.Clock()
shipimg = pygame.image.load('FreeShip.png')
shipwidth = 84
shipheight = 61
backgroundpic = pygame.image.load('background.jpg')
intro_background = pygame.image.load('intro_jpeg.jpg')
instruction_background = pygame.image.load('instruction_background.jpg')


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0, 0))
        button('START', 150, 520, 100, 50, green, bright_green, 'play')
        button('QUIT', 550, 520, 100, 50, red, bright_red, 'quit')
        button('INSTRUCTION', 300, 520, 200, 50, blue, bright_blue, 'intro')
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()

    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    gamedisplays.blit(textsurf, textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_objects("This is a space game where you need dodge the asteroids", smalltext)
        textRect.center = (350, 200)
        TextSurf, TextRect = text_objects("INSTRUCTIONS", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        gamedisplays.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : MOVE LEFT", smalltext)
        stextRect.center = (150, 400)
        utextSurf, utextRect = text_objects("ARROW UP : MOVE UP", smalltext)
        utextRect.center = (150, 500)
        dtextSurf, dtextRect = text_objects("ARROW UP : MOVE DOWN", smalltext)
        dtextRect.center = (150, 550)
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : MOVE RIGHT", smalltext)
        hTextRect.center = (150, 450)
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = (350, 300)
        gamedisplays.blit(sTextSurf, sTextRect)
        gamedisplays.blit(utextSurf, utextRect)
        gamedisplays.blit(dtextSurf, dtextRect)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(hTextSurf, hTextRect)
        button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")
        pygame.display.update()
        clock.tick(30)


def countdown_background():
    x = (display_width * 0.45)
    y = (display_height * 0.9)
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(shipimg, (x, y))

def countdown():
    countdown = True

    while countdown:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("3", largetext)
            TextRect.center = ((display_width/2), (display_height/2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("2", largetext)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("1", largetext)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("GO!!!", largetext)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()


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


intro_loop()
game_loop()
pygame.quit()
quit()
