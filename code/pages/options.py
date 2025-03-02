import pygame
from button2 import Button2
from settings import *
from button import Button

class Options:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Options")

        self.running = True
        self.clock = pygame.time.Clock()

        # Font for buttons
        self.font = pygame.font.Font(None, 36)

        # Define buttons
        self.pause_button = Button2(50, 100, 200, 50, "Pause Music", self.font, (255, 255, 255), (70, 120, 237))
        self.unpause_button = Button2(50, 200, 200, 50, "Unpause Music", self.font, (255, 255, 255), (108, 209, 112))
        self.stop_button = Button2(50, 300, 200, 50, "Stop Music", self.font, (255, 255, 255), (209, 108, 108))
        self.volume_up_button = Button2(300, 100, 200, 50, "Volume +", self.font, (255, 255, 255), (208, 150, 219))
        self.volume_down_button = Button2(300, 200, 200, 50, "Volume -", self.font, (255, 255, 255), (208, 150, 219))

        # Back button
        self.back_img = pygame.image.load("images/buttons/back.png").convert_alpha()
        self.back_button = Button("back", WINDOW_WIDTH / 2 - 45 * 3 - 20, 430, self.back_img, 7)

        # Current volume level
        self.volume = 0.5  # Default volume (50%)
        pygame.mixer.music.set_volume(self.volume)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Handle button clicks
                if self.pause_button.is_clicked(event):
                    pygame.mixer.music.pause()
                elif self.unpause_button.is_clicked(event):
                    pygame.mixer.music.unpause()
                elif self.stop_button.is_clicked(event):
                    pygame.mixer.music.stop()
                elif self.volume_up_button.is_clicked(event):
                    self.volume = min(1.0, self.volume + 0.1)  # Increase volume (max 1.0)
                    pygame.mixer.music.set_volume(self.volume)
                elif self.volume_down_button.is_clicked(event):
                    self.volume = max(0.0, self.volume - 0.1)  # Decrease volume (min 0.0)
                    pygame.mixer.music.set_volume(self.volume)

            # Draw the background
            bg = pygame.image.load("images/other/startscreen.png")
            self.window.blit(bg, (0, -300))

            # Draw back button
            if self.back_button.draw(self.window):
                from main import Game
                self.running = False  # Stop the options screen
                main = Game()
                main.run()  # Switch to the main screen

            # Draw other buttons
            self.pause_button.draw(self.window)
            self.unpause_button.draw(self.window)
            self.stop_button.draw(self.window)
            self.volume_up_button.draw(self.window)
            self.volume_down_button.draw(self.window)

            pygame.display.update()

        pygame.quit()
