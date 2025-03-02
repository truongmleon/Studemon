import pygame
from settings import *
import button
from start import Start

class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("Studemon")
        self.running = True

        # creating sprite goups
        self.all_sprites = pygame.sprite.Group()

        # create a clock object to help track frame rate
        self.clock = pygame.time.Clock()

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

            bg = pygame.image.load("images/other/startscreen.png")
            logo = pygame.image.load("images/logo/logo.png")
            self.window.blit(bg, (0, -300))
            self.window.blit(logo, (WINDOW_WIDTH / 5, 0))
            
            start_img = pygame.image.load("images/buttons/start.png").convert_alpha()  
            options_img = pygame.image.load("images/buttons/options.png").convert_alpha()  
            editset_img = pygame.image.load("images/buttons/editset.png").convert_alpha()  
            
            start_button = button.Button("start", WINDOW_WIDTH / 2 - 45 * 3 - 20, 300, start_img, 7)
            options_button = button.Button("options", WINDOW_WIDTH / 2 - 45 * 3 - 20, 430, options_img, 7)
            editset_button = button.Button("editset", WINDOW_WIDTH / 2 - 45 * 3 - 20, 560, editset_img, 7)
            
        
            if (start_button.draw(self.window)):
                start = Start()
                start.run()
            if (options_button.draw(self.window)):
                pass
            if (editset_button.draw(self.window)):
                pass
            # update sprites
            self.all_sprites.update(dt)

            # Draw sprites
            self.all_sprites.draw(self.window)

            # update the display
            pygame.display.update()
            
        pygame.quit()

    
# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
