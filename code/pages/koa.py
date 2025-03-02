import pygame
from settings import *

class Koa:
    def __init__(self):
        pygame.init()
        self.running = True

        # Set up the display
        self.window = pygame.display.set_mode((800, 600))  # Replace with WINDOW_WIDTH, WINDOW_HEIGHT if defined
        pygame.display.set_caption("Professor Koa")

        # Load the image
        self.image = pygame.image.load("Prof.png").convert_alpha()

    def run(self):
        """ Main game loop for Koa screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen (optional background color)
            self.window.fill((255, 255, 255))  # White background

            # Draw the image at a specified position
            self.window.blit(self.image, (100, 100))  # Adjust (100, 100) for your image's position

            # Update the display
            pygame.display.flip()

        pygame.quit()
