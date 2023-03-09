import pygame
import time
import sys
import os
from random import randint

pygame.init()
pygame.font.init()
# Display
WIDTH = 800
HEIGHT = 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

fps = pygame.time.Clock()
# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)
LIGHTBLUE = (100, 100, 255)
LIGHTGREEN = (100, 255, 100)

# Spieler "Kopf"
snake_pos = [10, 160]
snake2_pos = [10, 400]

# Spielerkörper
snake_body = [[10, 160],
              [10, 150],
              [10, 140],
              [10, 130]
              ]
snake2_body = [[10, 400],
               [10, 390],
               [10, 380],
               [10, 370]
               ]

# Geschwindigkeit und Richtung
snake_speed = 12
snake_direction = "RIGHT"
change_direction = "RIGHT"
snake2_direction = "RIGHT"
change2_direction = "RIGHT"
score = 0
score2 = 0


def neustart():
    global snake_pos, snake2_pos, snake_body, snake2_body, snake_direction, change_direction, snake2_direction, change2_direction, score, score2
    print("NEUSTART")
    snake_pos = [10, 160]
    snake2_pos = [10, 400]
    snake_body = [[10, 160],
                  [10, 150],
                  [10, 140],
                  [10, 130]
                  ]
    snake2_body = [[10, 400],
                   [10, 390],
                   [10, 380],
                   [10, 370]
                   ]
    snake_direction = "RIGHT"
    change_direction = "RIGHT"
    snake2_direction = "RIGHT"
    change2_direction = "RIGHT"
    score = 0
    score2 = 0


def directiontest(current_dir, change_to_dir):
    if change_to_dir == "LEFT" and current_dir != "RIGHT":
        current_dir = "LEFT"
    if change_to_dir == "DOWN" and current_dir != "UP":
        current_dir = "DOWN"
    if change_to_dir == "RIGHT" and current_dir != "LEFT":
        current_dir = "RIGHT"
    if change_to_dir == "UP" and current_dir != "DOWN":
        current_dir = "UP"
    return current_dir


def kollision_check(head, body, head2):
    global snake_pos, snake2_pos
    if head[0] == -10 or head[0] == 800 or head[1] == -10 or head[1] == 600:
        if head == snake_pos:
            win_screen(2)
            print("Wand!")
        else:
            win_screen(1)

    for block in body[1:]:
        if block[0] == head[0] and block[1] == head[1]:
            print("Auto-Kannibalismus!")
            if head == snake_pos:
                win_screen(2)
            else:
                win_screen(1)

    for block in body:
        if block[0] == head2[0] and block[1] == head2[1]:
            if head == snake_pos:
                win_screen(1)
            else:
                win_screen(2)
            print("Crash")
    if head[0] == head2[0] and head[1] == head2[1]:
        win_screen(0)
        print("crash2")



def steuerung(hoch, rechts, runter, links, aktuell, event):
    direction = aktuell

    if event.key == hoch:
        direction = "UP"
    if event.key == rechts:
        direction = "RIGHT"
    if event.key == runter:
        direction = "DOWN"
    if event.key == links:
        direction = "LEFT"

    return direction


def new_apple():
    global apple_pos
    apple_pos = [10 * randint(0, int(WIDTH / 10) - 1), 10 * randint(0, int(HEIGHT / 10) - 1)]
    print("apple x:", apple_pos[0])
    print("apple_y:", apple_pos[1])


new_apple()

def pause():
    global snake_speed
    is_running = True
    while is_running:
        DISPLAY.fill(BLACK)
        font = pygame.font.Font(None, 30)



        for i in snake_body:
            pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((i[0], i[1], 10, 10)), 2)

        for i in snake2_body:
            pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((i[0], i[1], 10, 10)), 2)

        text_darstellen(340,450,"- Pause -",WHITE,font)
        score_text= "Score: "+str(score)
        text_darstellen(10,10,score_text,WHITE,font)
        score2_text= "Score: "+str(score2)
        text_darstellen(706,10,score2_text,WHITE,font)
        speed_text = "Geschwindigkeit:"+str(snake_speed)
        text_darstellen(10,50,speed_text,WHITE,font)

        pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((10, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((706, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, RED, (apple_pos[0], apple_pos[1], 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    neustart()
                    menu()
                else:
                    game()

        pygame.display.update()

def move_snake(direction,pos):
    if direction == "UP":
        pos[1] -= 10
    elif direction == "RIGHT":
        pos[0] += 10
    elif direction == "DOWN":
        pos[1] += 10
    elif direction == "LEFT":
        pos[0] -= 10
    return pos

def text_darstellen(x,y,text,farbe,font):
    anzeige_text = font.render(text, True, farbe)
    DISPLAY.blit(anzeige_text, (x, y))

def game():
    global snake_pos, snake2_pos, snake_body, snake2_body, snake_direction, change_direction, snake2_direction, change2_direction, score, score2
    is_running = True
    while is_running:
        DISPLAY.fill(BLACK)
        font = pygame.font.Font(None, 30)


        snake_direction = directiontest(snake_direction, change_direction)
        snake2_direction = directiontest(snake2_direction, change2_direction)

        snake_pos = move_snake(snake_direction,snake_pos)
        snake2_pos = move_snake(snake2_direction, snake2_pos)



        # Kollision Schlange-Wand & Schlange-Schlange
        kollision_check(snake_pos, snake_body, snake2_pos)
        kollision_check(snake2_pos, snake2_body, snake_pos)


        # Wachstumsmechanismus
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            score += 10
            print(score)
            new_apple()
        else:
            snake_body.pop()

        # Wachstumsmechanismus 2
        snake2_body.insert(0, list(snake2_pos))
        if snake2_pos[0] == apple_pos[0] and snake2_pos[1] == apple_pos[1]:
            score2 += 10
            print(score2)
            new_apple()
        else:
            snake2_body.pop()

        # Score darstellen
        score_text= "Score: "+str(score)
        text_darstellen(10,10,score_text,WHITE,font)
        score2_text= "Score: "+str(score2)
        text_darstellen(706,10,score2_text,WHITE,font)

        pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((10, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((706, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, RED, (apple_pos[0], apple_pos[1], 10, 10))

        # Schlange zeichnen
        for i in snake_body:
            pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((i[0], i[1], 10, 10)), 2)

        for i in snake2_body:
            pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((i[0], i[1], 10, 10)), 2)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                    is_running = False

                change_direction = steuerung(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a, change_direction, event)
                change2_direction = steuerung(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, change2_direction, event)
        pygame.display.update()
        fps.tick(snake_speed)


def menu():
    global snake_speed
    is_running = True
    while is_running:
        DISPLAY.fill(BLACK)
        font = pygame.font.Font(None, 30)



        for i in snake_body:
            pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((i[0], i[1], 10, 10)), 2)

        for i in snake2_body:
            pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((i[0], i[1], 10, 10)), 2)

        text_darstellen(160,500,"- Drücken sie eine beliebige Taste um zu starten -",WHITE,font)
        score_text= "Score: "+str(score)
        text_darstellen(10,10,score_text,WHITE,font)
        score2_text= "Score: "+str(score2)
        text_darstellen(706,10,score2_text,WHITE,font)
        speed_text = "Geschwindigkeit:"+str(snake_speed)+"  +[p]  -[m]"
        text_darstellen(10,50,speed_text,WHITE,font)

        pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((10, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((706, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, RED, (apple_pos[0], apple_pos[1], 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_p:
                    if snake_speed < 30:
                        snake_speed += 1
                elif event.key == pygame.K_m:
                    if snake_speed >1:
                        snake_speed -= 1
                else:
                    game()

        pygame.display.update()


def win_screen(win):
    global score, score2
    is_running = True
    text = ""
    print("win:" ,win)
    if win == 0:
        text = "Unentschieden"
        if score > score2:
            text = "Spieler 1 hat gewonnen"
        elif score < score2:
            text = "Spieler 2 hat gewonnen"
    elif win == 1:
        text = "Spieler 1 hat gewonnen"
    elif win == 2:
        text = "Spieler 2 hat gewonnen"

    while is_running:
        DISPLAY.fill(BLACK)
        font = pygame.font.Font(None, 30)

        for i in snake_body:
            pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((i[0], i[1], 10, 10)), 2)
        for i in snake2_body:
            pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((i[0], i[1], 10, 10)), 2)

        text_darstellen(310,200,text,WHITE,font)
        score_text= "Score: "+str(score)
        text_darstellen(10,10,score_text,WHITE,font)
        score2_text= "Score: "+str(score2)
        text_darstellen(706,10,score2_text,WHITE,font)

        pygame.draw.rect(DISPLAY, LIGHTGREEN, pygame.Rect((10, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, LIGHTBLUE, pygame.Rect((706, 30, 78, 5)), 2)
        pygame.draw.rect(DISPLAY, RED, (apple_pos[0], apple_pos[1], 10, 10))
        pygame.display.update()
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    neustart()
                    menu()
                else:
                    is_running = False
                    neustart()


        pygame.display.update()



menu()
pygame.quit()
