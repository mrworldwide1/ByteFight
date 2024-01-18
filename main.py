# Name: ByteFight
# Description: ICS4U SDLC summative project, a game inspired by Math prodigy.
# Date: November 28, 2023
# By: Omar S, Lucas L, Harris V
# some features like soundtrack dont work on replit - check the github

import pygame
import sys
import time
import random
from button import Button
from cs_questions import computer_science_questions

## Setup ##

# other variables so nothing is hardcoded
game_name = "ByteFight"

# setup display
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
programIcon = pygame.image.load('battle_arena.png').convert_alpha() # load icon image as a Surface then change icon
pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()

# get fonts
title_font_size = 72
title_font = pygame.font.Font('Retro Gaming.ttf', title_font_size)
button_font_size = 36
button_font = pygame.font.Font('Retro Gaming.ttf', button_font_size)
tiny_font_size = 18
tiny_font = pygame.font.Font('Retro Gaming.ttf', tiny_font_size)
character_font_size = 14 
character_font = pygame.font.Font('Retro Gaming.ttf', character_font_size)

# Health bar variables
health_bar_colour_one = (255, 0, 0)
health_bar_colour_two = (0, 255, 0)

# Music that may play in battle - each time player clicks play, pick a random song
battleSoundtracks = ["xDeviruchi - Decisive Battle.wav", "xDeviruchi - And The Journey Begins .wav", "xDeviruchi - The Icy Cave .wav"]

# Displays text onto screen surface
def display_text(text, font, x, y, colour):
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function that fits background image onto entire screen
def display_background(image):
    bg = pygame.image.load(image).convert_alpha()
    bg = pygame.transform.scale(bg, (screen_width, screen_height))
    screen.blit(bg, (0, 0))

# custom function to play soundtracks
def play_soundtrack(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1, 0, 4000)

# custom function that fades out whatevers currently playing
def stop_soundtrack():
    pygame.mixer.music.fadeout(1000)


def title_screen():
  # play music
  stop_soundtrack()
  play_soundtrack("xDeviruchi - Title Theme .wav")

  while True:
      # Title and Background
      display_background('title_screen_bg.jpg')
      display_text(game_name, title_font, screen_width/2, screen_height/6, 'white')
      display_text("By: Lucas L, Omar S, Harris V", tiny_font, screen_width/2, screen_height/1.1, 'white') # Name rights
      
    # Menu choices
      computer_science_button = Button("Play", button_font, screen_width/14, screen_height/2.5, "green", "white", 120, 50)
      quit_button = Button("Quit", button_font, screen_width/14, screen_height/1.8, "red", "white", 120, 50)
      computer_science_button.display()
      quit_button.display()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
        # switch game state if buttons clicked 
          elif event.type == pygame.MOUSEBUTTONUP:
              if computer_science_button.collide():
                  computer_science_arena()
              elif quit_button.collide():
                  pygame.quit()
                  sys.exit()

      # Updates everything
      pygame.display.update()
      clock.tick(60)


def computer_science_arena():
    # Sets enemy and player health points 
    player_health = 100 
    enemy_health = 100
    asked_questions = []

    # play music
    stop_soundtrack()
    play_soundtrack(random.choice(battleSoundtracks))

    while True:
        display_background('battle_arena.png')  # Displays battle arena
      
        # Displays health bars
        pygame.draw.rect(screen, health_bar_colour_two, (20, 20, player_health * 2.2, 30))
        pygame.draw.rect(screen, health_bar_colour_one, (400, 20, enemy_health * 2.2, 30))
      
        # Displays player and enemy names 
        display_text('Wizard', character_font, 50, 10, 'white')
        display_text('Earth Creature', character_font, 465, 10, 'white')
      
        # Displays fight and heal buttons
        fight_button = Button("Fight", button_font, screen_width / 12, screen_height - 100, "brown", "white", 120, 50)
        heal_button = Button("Heal", button_font, 3 * screen_width / 4.10, screen_height - 100, "brown", "white", 120, 50)
        fight_button.display()
        heal_button.display()
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:

                # ask questions when fight clicked
                if fight_button.collide():
                    while True: 
                        question_data = random.choice(computer_science_questions)
                        if question_data["question"] not in asked_questions:
                            asked_questions.append(question_data["question"])  # Ensures the same question is not asked twice
                            break

                    question = question_data["question"]
                    options = question_data["options"]
                    answer = input(f"{question} ({', '.join(options)}: ")
                     
                    if answer.upper() == question_data["answer"]:
                        enemy_health -= random.randint(10, 20) # Attacks enemy if correct answer 
                        print("You attacked!")
                    else:
                        damage = random.randint(10, 20) # Damages player if incorrect answer
                        player_health -= damage
                        if damage > 15: 
                            print("Enemy lands crit! You missed!") # Displays message if enemy lands critical hit
                        else:
                            print("Enemy lands hit! You missed!") # Displays message if enemy lands hit 
                          
                # ask questions if heal clicked
                elif heal_button.collide():
                    question_data = random.choice(computer_science_questions)
                    question = question_data["question"]
                    options = question_data["options"]
                    answer = input(f"{question} ({', '.join(options)}: ")

                    if answer.upper() == question_data["answer"]:
                        player_health += random.randint(5, 10)
                        player_health = min(100, player_health)
                        print("You healed!")
                    else:
                        damage = random.randint(15, 60)
                        player_health -= damage
                        if damage > 20:
                            print("You missed!") 
                        else:
                            print("Enemy Lands Hit! You missed! ") 
                          
        # Displays game over or victory screen
        if player_health <= 0:
            display_text("Game Over", title_font, screen_width / 2, screen_height / 1.5, 'red')
            pygame.display.update()
            time.sleep(2)
            return
        elif enemy_health <= 0:
            display_text("You Win!", title_font, screen_width / 2, screen_height / 2, 'green')
            pygame.display.update()
            time.sleep(2)
            return

        # Updates everything
        pygame.display.update()
        clock.tick(60)

# Starts game 
title_screen()