import pygame
from settings import *
import button

# pygame setup
class Game:
    def __init__(self):

        # initialize pygame
        pygame.init()

        # create window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Studemon")
        self.running = True

        # creating sprite goups
        self.all_sprites = pygame.sprite.Group()

        # create a clock object to help track frame rate
        self.clock = pygame.time.Clock()
        
        # player position (center of the screen)
        self.player_pos = pygame.Vector2(self.window.get_width() / 2, self.window.get_height() / 2)
        
        self.bg = pygame.image.load("path/to/background_image.png").convert_alpha()
        self.button_img = pygame.image.load("path/to/button_image.png").convert_alpha()
        

    def handle_events(self):
        """ Handle events """
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
            
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                    
    def render(self):
        """ Draw everything """
        # Draw the background
        self.window.blit(self.bg, (0, -300))
        
        # Draw the button
        self.draw(self.window, (255, 0, 0))
        
        # Draw the player
        pygame.draw.circle(self.window, COLORS['black'], self.player_pos, 10)
        
        self.all_sprites.draw(self.window)
        
        pygame.display.flip()
        
    def update(self):
        self.all_sprites.update(self.dt)

    def run(self):
        """ Game loop """
        while self.running:

            # Controling the frame rate to 60 FPS
            self.clock.tick(60) / 1000

            self.handle_events()
            self.update()
            self.render()
            # update the display
            pygame.display.update()
            
        pygame.quit()

    
# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
