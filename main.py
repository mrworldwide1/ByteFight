# Name: Prodigy
# Description: ICS4U SDLC summative project, a game inspired by Math prodigy.
# Date: November 28, 2023
# By: Omar S, Lucas L, Harris V

import pygame, sys, time
from button import Button

## Setup ##

# setup display
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prodigy")
clock = pygame.time.Clock()

# get fonts
title_font_size = 72
title_font = pygame.font.Font('Retro Gaming.ttf', title_font_size)
button_font_size = 36
button_font = pygame.font.Font('Retro Gaming.ttf', button_font_size)

# other variables so nothing is hardcoded
game_name = "Prodigy"

# questions
math_questions = []
computer_science_questions = []

# custom function that quickly puts text onto screen surface
def display_text(text, font, x, y, colour):
    text_surface = font.render(text, True, colour)
    # align with rect
    text_rect = text_surface.get_rect(center = (x, y))
    screen.blit(text_surface, text_rect)

# custom function that fits image onto entire screen
def display_background(image):
    bg = pygame.image.load(image).convert_alpha()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0,0))

# custom function to play soundtracks
def play_soundtrack(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1, 0, 4000)

# custom function that fades out whatevers currently playing
def stop_soundtrack():
    pygame.mixer.music.fadeout(1000)


## Game States as functions to switch between different menus ##
def title_screen():

    play_soundtrack("xDeviruchi - Title Theme .wav")

    while True:
        display_background('title_screen_bg.jpg')
        display_text(game_name, title_font, screen_width/2, screen_height/6, 'white')

        # menu choices
        math_button = Button("Math", button_font, screen_width/14, screen_height/2.5, "brown", "white", 125, 50)
        computer_science_button = Button("Computer Science", button_font, screen_width/14, screen_height/1.8, "brown", "white", 420, 50)
        science_button = Button("Science", button_font, screen_width/14, screen_height/1.4, "brown", "white", 190, 50)
        math_button.display()
        computer_science_button.display()
        science_button.display()

        # switch game states based on buttons pressed
        if math_button.clicked():
            stop_soundtrack()
            math_arena()
        elif computer_science_button.clicked():
            stop_soundtrack()            
            computer_science_arena()
        elif science_button.clicked():
            stop_soundtrack()
            science_arena()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update everything
        pygame.display.update()
        clock.tick(60)

def math_arena():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display_background('math_arena.jpg')

        pygame.display.update()
        clock.tick(60)

def computer_science_arena():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display_background('computer_science_arena.png')

        pygame.display.update()
        clock.tick(60)

def science_arena():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display_background('science_arena.png')

        pygame.display.update()
        clock.tick(60)


# actually starts the game
title_screen()