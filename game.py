import pygame
import random
import os
import time
# background music
pygame.mixer.init()
pygame.mixer.music.load("game on.mp3")
pygame.mixer.music.play()
pygame.init()
# window
win_width = 400
win_height = 600
enemy_width = 80
enemy_width2 = 260
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Car Crash")
pygame.display.update()
# back image
background = pygame.image.load("road3.jpg")
background = pygame.transform.scale(background,(win_width,win_height)).convert_alpha()
# enemy
enemy_x = random.randint(enemy_width,enemy_width2)
enemy_y = random.randint(0, 0)
size = 40
# car image
car_img = pygame.image.load("car7.png")
enemy_img = pygame.image.load("car.png")
def car_image(a,b):
    win.blit(car_img, (car_x, car_y))

def enemy_car():
    win.blit(enemy_img,(enemy_x, enemy_y))
# font size
font = pygame.font.SysFont(None,50)
# functions
def text_screen(text,colour,x,y):
    screen_text = font.render(text, True, colour)
    win.blit(screen_text, (x, y))

def plot_car(win,color,enemy2,enemy,size,size2):
    pygame.draw.rect(win,color,[enemy2,enemy,size,size2])
clock = pygame.time.Clock()

def play_music():
    pygame.mixer.music.load("game on.mp3")
    pygame.mixer.music.play()

# colors
white = [255,255,255]
black = [0,0,0]
purple = [200,45,145]
yellow = [255,255,45]
green = [145,214,65]
red = [255,0,0]
# game loop

fps = 30
exit_game = False
game_over = False
car_x = 180
car_y = 470
road_x = 0
road_y = 0
enemy_x = random.randint(enemy_width,enemy_width2)
enemy_y = random.randint(0, 0)

# game loop
while not exit_game:
    if game_over:
        win.fill(black)
        text_screen('GAME OVER', red, 100, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        car_x = car_x + 30
                if event.key == pygame.K_LEFT:
                        car_x = car_x - 30

        enemy_y = enemy_y + 15
        road_y = road_y + 10

        if abs(car_x - enemy_x) < 35 and abs(car_y - enemy_y) < 35:
                    game_over = True  # game over statement
                    pygame.mixer.music.load("car_crash.mp3")
                    pygame.mixer.music.play()

        if car_x < enemy_width or car_x > enemy_width2 or car_y < 0 or car_y > win_height:
                    game_over = True  # game over statement
                    pygame.mixer.music.load("car_crash.mp3")
                    pygame.mixer.music.play()
        if enemy_x < enemy_width or enemy_x > enemy_width2 or enemy_y < 0 or enemy_y > win_height:
                enemy_y = 0
                enemy_x = random.randint(enemy_width,enemy_width2)

        if road_y == 600:
            road_y = 0

        win.blit(background,(0, 0))
        win.fill(yellow)
                # moving background
        win.blit(background,[road_x,road_y - 600])
        win.blit(background, [road_x, road_y])
        car_image(car_x,car_y)
        enemy_car()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()