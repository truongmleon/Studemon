import pygame
from settings import *

class Result:
    def __init__(self, result):
        pygame.init()
        self.running = True
        self.font = pygame.font.Font(None, 25)

        # Set up the display
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
        pygame.display.set_caption("Results")
        bg_win = pygame.image.load("images/other/Win.png")
        bg_lose = pygame.image.load("images/other/Lose.png")
        if result == 1:
            self.window.blit(bg_win, (0, 0))
        else:
            self.window.blit(bg_lose, (0, 0))

    def run(self):
        """ Main game loop for Koa screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


                # Update the display
                pygame.display.flip()

        pygame.quit()
        