import pygame
from settings import *
import button

class Start:
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
    game = Start()
    game.run()
