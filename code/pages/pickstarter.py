import pygame
from settings import *
from battle import Battle

class PickStarter:
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
        pygame.display.set_caption("Kevin Nguyen")

        # Load the image
        self.image = pygame.image.load("images/characters/Prof.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 21), int(self.image.get_height() * 21)))

        self.frone_img = pygame.image.load("images/studemon-sprites/Frone.png").convert_alpha() 
        self.frone_img = pygame.transform.scale(self.frone_img, (int(self.frone_img.get_width() * 0.75), int(self.frone_img.get_height() * 0.75)))
        self.window.blit(self.frone_img, (950, 460))

        self.intiggy_img = pygame.image.load("images/studemon-sprites/Intiggy.png").convert_alpha() 
        self.intiggy_img = pygame.transform.scale(self.intiggy_img, (int(self.intiggy_img.get_width() * 0.75), int(self.intiggy_img.get_height() * 0.75)))
        self.window.blit(self.intiggy_img, (100, 450))

        self.noed_img = pygame.image.load("images/studemon-sprites/Noed.png").convert_alpha() 
        self.noed_img = pygame.transform.scale(self.noed_img, (int(self.noed_img.get_width() * 0.75), int(self.noed_img.get_height() * 0.75)))
        self.window.blit(self.noed_img, (500, 520))

    def run(self):
        """ Main game loop for pick starter screen """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Handle key presses for picking a starter
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.player_choice = 1  # Save the player's choice as 1
                        self.running = False  # Exit the loop to finalize the choice
                    elif event.key == pygame.K_2:
                        self.player_choice = 2  # Save the player's choice as 2
                        self.running = False
                    elif event.key == pygame.K_3:
                        self.player_choice = 3  # Save the player's choice as 3
                        self.running = False

            bg = pygame.image.load("images/other/Lab.png")
            self.window.blit(bg, (0, 0))
            textbox = pygame.image.load("images/buttons/textbox.png").convert_alpha()
            textbox = pygame.transform.scale(textbox, (int(textbox.get_width() * 9), int(textbox.get_height() * 9)))
            self.window.blit(self.frone_img, (950, 410))
            self.window.blit(self.intiggy_img, (100, 400))
            self.window.blit(self.noed_img, (500, 470))
            self.window.blit(textbox, (100, 100))
            
            
            self.draw_text("Go ahead and pick a STUDÉMON!", 130, 120)

            self.draw_text("Press 1 for Intiggy", 150, 350)
            self.draw_text("Press 2 for Noed", 550, 350)
            self.draw_text("Press 3 for Frone", 1000, 350)
            
            # Update the display
            pygame.display.flip()

        battle = Battle(self.data, self.player_choice)
        battle.run()
        
    def draw_text(self, text, x, y):
        """ Helper function to draw text on the screen """
        text_surface = self.font.render(text, True, self.text_color)
        self.window.blit(text_surface, (x, y))