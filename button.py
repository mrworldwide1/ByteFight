import pygame

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# menu button
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

    # return whether mouse touching and clicked, also stops player from holding it down
    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            if self.locked == False:
                self.locked = True
                return True
        else:
            self.locked = False
            return False