import pygame
from settings import *
from support import *
from monster import Monster, Oponent
from ui import UI
from random import choice
import button


class Battle:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Studemon")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # Creating sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        # Data
        player_studemon_list = ['Nod'] #change this when sprites
        #                                                    Change 'shrek' to "name" when implement
        self.player_studemon = [Monster(name, self.back_surfs.get(name, self.back_surfs['shrek'])) for name in player_studemon_list]
        self.monster = self.player_studemon[0]
        self.all_sprites.add(self.monster)
        #oponent_name = choice(list(MONSTER_DATA.keys()))
        self.oponent = Oponent("Frubber", self.back_surfs['shrek'], self.all_sprites)
        
        # UI
        self.ui = UI(self.monster)

    def import_assets(self):
        self.back_surfs = folder_importer('images', 'logo')  # Store images as a dictionary
        self.front_sufs = folder_importer('images', 'logo')
        self.bg_surfs = folder_importer('images', 'other')

    def run(self):
        """ Game loop """
        zoom_factor = 1.40  # Zoom in by 2x
        bg_image = self.bg_surfs['battlebg']  # Original background
        bg_width, bg_height = bg_image.get_size()
        
        # Scale the background to simulate zooming
        zoomed_bg = pygame.transform.scale(bg_image, (int(bg_width * zoom_factor), int(bg_height * zoom_factor)))

        # Calculate the top-right area of the zoomed background to blit
        crop_x = int(bg_width * (zoom_factor - 1))  # Start from the top-right corner
        crop_y = int(bg_height * 0.3)  # Top-right means Y starts at 0
        crop_width = WINDOW_WIDTH  # Match the display width
        crop_height = WINDOW_HEIGHT  # Match the display height
        
        # Create a Rect for the area of the zoomed background to display
        crop_rect = pygame.Rect(crop_x, crop_y, crop_width, crop_height)

        while self.running:
            # Controling the frame rate and get the delta (dt) in seconds
            dt = self.clock.tick() / 1000
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Draw the cropped section of the zoomed background
            self.window.blit(zoomed_bg, (0, 0), crop_rect)

            # update sprites
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.window)

            # Draw sprites
            
            
            # Might have to change this later becuase we will put shrek2 out there later
            # player_pos = pygame.Vector2(self.window.get_width() / 2, self.window.get_height() / 2)    
            # bg = pygame.image.load("images/logo/shrek.jpg")
            # self.window.blit(bg, (600, 300)) 
            
            self.all_sprites.draw(self.window)
            self.ui.draw()

            # update the display
            pygame.display.update()
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Battle()
    game.run()

