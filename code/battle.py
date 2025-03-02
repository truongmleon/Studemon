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
        while self.running:
            # Controling the frame rate and get the delta (dt) in seconds
            dt = self.clock.tick() / 1000
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            

            # update sprites
            self.all_sprites.update(dt)

            # Draw sprites
            self.window.blit(self.bg_surfs['battlebg'], (0, 0))
            
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

