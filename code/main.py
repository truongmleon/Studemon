import pygame
from settings import *
import button
from pages.start import Start
from pages.options import Options
from pages.lab import Lab

class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("Studemon")
        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:

            # Controling the frame rate and get the delta (dt) in seconds
            dt = self.clock.tick() / 1000

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            player_pos = pygame.Vector2(self.window.get_width() / 2, self.window.get_height() / 2)    

            bg = pygame.image.load("images/other/startscreen.png")
            logo = pygame.image.load("images/logo/logo.png")
            self.window.blit(bg, (0, -300))
            self.window.blit(logo, (WINDOW_WIDTH / 5, 0))
            
            start_img = pygame.image.load("images/buttons/start.png").convert_alpha()  
            options_img = pygame.image.load("images/buttons/options.png").convert_alpha()  
                        
            start_button = button.Button("start", WINDOW_WIDTH / 2 - 45 * 3 - 20, 300, start_img, 7)
            options_button = button.Button("options", WINDOW_WIDTH / 2 - 45 * 3 - 20, 430, options_img, 7)

            frone_img = pygame.image.load("images/studemon-sprites/Frone Thumbnail.png").convert_alpha() 
            frone_img = pygame.transform.scale(frone_img, (int(frone_img.get_width() * 0.75), int(frone_img.get_height() * 0.75)))
            self.window.blit(frone_img, (950, 460))

            intiggy_img = pygame.image.load("images/studemon-sprites/Intiggy Thumbnail.png").convert_alpha() 
            intiggy_img = pygame.transform.scale(intiggy_img, (int(intiggy_img.get_width() * 0.75), int(intiggy_img.get_height() * 0.75)))
            self.window.blit(intiggy_img, (100, 450))

            noed_img = pygame.image.load("images/studemon-sprites/Noed Thumbnail.png").convert_alpha() 
            noed_img = pygame.transform.scale(noed_img, (int(noed_img.get_width() * 0.75), int(noed_img.get_height() * 0.75)))
            self.window.blit(noed_img, (500, 520))

            if (start_button.draw(self.window)):
                start = Start()
                start.run()
            if (options_button.draw(self.window)):
                options = Options()
                options.run()

            self.all_sprites.update(dt)
            self.all_sprites.draw(self.window)

            pygame.display.update()
            
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
