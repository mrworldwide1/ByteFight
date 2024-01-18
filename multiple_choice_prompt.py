# Custom class made to show multiple choice player input

import pygame

# values from main.py so that no errors arise
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# class inherits features from pygame Sprite class
class Multiple_Choice_Prompt(pygame.sprite.Sprite):
    def __init__(self, x, y, colour, text):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface
        