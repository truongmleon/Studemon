import pygame
from settings import *

class Koa:
    def __init__(self, data):
        pygame.init()
        self.to_kevin = False
        self.to_next_oak = False
        self.data = data
        self.running = True
        self.font = pygame.font.Font(None, 25)
        self.text_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.box_color_inactive = (200, 200, 200)
        self.box_color_active = (255, 255, 255)

        # Set up the display
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
        pygame.display.set_caption("Professor Koa")

        # Load the image
        self.image = pygame.image.load("images/characters/Prof.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 21), int(self.image.get_height() * 21)))

    def run(self):
        """ Main game loop for Koa screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((255, 255, 255))  # White background
            textbox = pygame.image.load("images/buttons/textbox.png").convert_alpha()
            textbox = pygame.transform.scale(textbox, (int(textbox.get_width() * 9), int(textbox.get_height() * 9)))
            self.window.blit(self.image, (470, -80))
            self.window.blit(textbox, (100, 100))
            
            
            self.draw_text("WHAT’S GOOD! Welcome to the world of STUDÉMON! My name is KOA!,", 130, 120)
            self.draw_text("People call me the STUDÉMON GANGSTA! This world is inhabited by", 130, 140)
            self.draw_text("creatures called STUDÉMON! For some STUDÉMON are pets. For you,", 130, 160)
            self.draw_text("you have been doing bad in school, so you are sent here! Myself,", 130, 180)
            self.draw_text("I’m your underpaid tutor who studies STUDÉMON on the side.", 130, 200)
            self.draw_text("First, what is your name?", 130, 220)
            
            # Update the display
            pygame.display.flip()

        pygame.quit()
        
    def draw_text(self, text, x, y):
        """ Helper function to draw text on the screen """
        text_surface = self.font.render(text, True, self.text_color)
        self.window.blit(text_surface, (x, y))