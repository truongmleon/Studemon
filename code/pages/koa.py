import pygame
from settings import *

class Koa:
    def __init__(self, data):
        pygame.init()
        self.data = data
        self.running = True

        # Set up the display
        self.window = pygame.display.set_mode((800, 600))  # Replace with WINDOW_WIDTH, WINDOW_HEIGHT if defined
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

            # Clear the screen (optional background color)
            self.window.fill((255, 255, 255))  # White background

            # Draw the image at a specified position
            self.window.blit(self.image, (170, -80)) 

            # Update the display
            pygame.display.flip()

        pygame.quit()
