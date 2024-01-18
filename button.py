# Custom class created to make it easier to add buttons in game.
# because pygame has an obtuse way of handling what is basically layers in photoshop

import pygame

# values from main.py so that no errors arise
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

class Button():
    def __init__(self, text, font, x, y, button_colour, font_colour, width, height):
        super().__init__()
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.button_colour = button_colour
        self.font_colour = font_colour
        self.width = width
        self.height = height
        self.locked = False
        
        # allign mid-left of text to mid-left of button
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_surface = self.font.render(self.text, False, self.font_colour)
        self.text_rect = self.text_surface.get_rect(midleft = self.rectangle.midleft)

    # create rectangle, draw text ontop then place onto screen
    def display(self):
        pygame.draw.rect(screen, self.button_colour, self.rectangle)
        screen.blit(self.text_surface, self.text_rect)

    # return whether mouse touching
    def collide(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mouse_pos):
            return True
        else:
            return False