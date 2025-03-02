import pygame
from settings import *
from pages.lab import Lab

class Kevin:
    def __init__(self, data):
        pygame.init()
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
        
        self.kev = pygame.image.load("images/characters/Kevin.png").convert_alpha()
        self.kev = pygame.transform.scale(self.kev, (int(self.kev.get_width() * 10), int(self.kev.get_height() * 10)))

    def run(self):
        """ Main game loop for Koa screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.window.fill((255, 255, 255))  # White background
                textbox = pygame.image.load("images/buttons/textbox.png").convert_alpha()
                textbox = pygame.transform.scale(textbox, (int(textbox.get_width() * 6), int(textbox.get_height() * 6)))
                self.window.blit(self.image, (470, -80))
                self.window.blit(self.kev, (100, 300))
                self.window.blit(textbox, (180, 100))
                self.window.blit(textbox, (140, 210))
                
                self.draw_text("Right! I’m not paid enough to care. This is", 210, 120)
                self.draw_text("my grandson. He's been your rival since you ", 210, 140)
                self.draw_text("were a baby, Kevin Nguyen-", 210, 160)
                
                self.draw_text("I LOVE KESHI AND ICE COFFEE BOBA!!", 160, 230)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    lab = Lab()
                    lab.run()

                # Update the display
                pygame.display.flip()

        pygame.quit()
        
    def draw_text(self, text, x, y):
        """ Helper function to draw text on the screen """
        text_surface = self.font.render(text, True, self.text_color)
        self.window.blit(text_surface, (x, y))