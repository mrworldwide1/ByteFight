# Custom class made to show multiple choice player input

import pygame
from cs_questions import computer_science_questions

# values from main.py so that no errors arise
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# class inherits features from pygame Sprite class
class Multiple_Choice_Prompt(pygame.sprite.Sprite):
    def __init__(self, x, y, colour, text):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface



# pseudocode
# display four rectangles on screen at specific x and y coords
# overlay text on those rectangles
        # text is taken using same code in main.py
# detect collision of those rectangles