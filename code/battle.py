import pygame
from settings import *
from support import *
from timer import Timer
import button


class Battle:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("Studemon")
        
         # create a clock object to help track frame rate
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.import_assets()

        # creating sprite goups
        self.all_sprites = pygame.sprite.Group()
        
        # data
        player_studemon_list = ['Nod']
        self.player_studemon = [Monster(name, self.back_surf(name)) for name in player_studemon_list]

    def import_assets(self):
        self.back_surf = folder_importer('images', 'logo', 'shrek.jpg')
        print(self.back_surf)


    def run(self):
        """ Game loop """
        while self.running:

            # Controling the frame rate and get the delta (dt) in seconds
            dt = self.clock.tick() / 1000

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            player_pos = pygame.Vector2(self.window.get_width() / 2, self.window.get_height() / 2)    
            bg = pygame.image.load("images/logo/shrek.jpg")

            self.window.blit(bg, (0, 0))            

            # update sprites
            self.all_sprites.update(dt)

            # Draw sprites
            self.all_sprites.draw(self.window)

            # update the display
            pygame.display.update()
            
        pygame.quit()

    
# Run the game
if __name__ == "__main__":
    game = Battle()
    game.run()
