import pygame
from settings import *

class Lab:
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

            bg = pygame.image.load("images/other/Lab.png")
            self.window.blit(bg, (0, 0))

            img = pygame.image.load("images/characters/Kevin.png").convert_alpha() 
            img = pygame.transform.scale(img, (int(img.get_width() * 4), int(img.get_height() * 4)))
            self.window.blit(img, (900, 450))

            profImg = pygame.image.load("images/characters/Prof.png").convert_alpha() 
            profImg = pygame.transform.scale(profImg, (int(profImg.get_width() * 4), int(profImg.get_height() * 4)))
            self.window.blit(profImg, (500, 250))

            self.all_sprites.update(dt)

            self.all_sprites.draw(self.window)

            pygame.display.update()
            
        pygame.quit()
