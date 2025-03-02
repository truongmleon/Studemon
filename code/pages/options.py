import pygame
from settings import *

class Options:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("Studemon")
        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            bg = pygame.image.load("images/other/startscreen.png")
            self.window.blit(bg, (0, -300))

            self.all_sprites.update(dt)

            self.all_sprites.draw(self.window)

            pygame.display.update()
            
        pygame.quit()
