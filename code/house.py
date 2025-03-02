import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
screen_width, screen_height = 1280, 720 # Adjust to fit your game's resolution
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the background image
background_image = pygame.image.load("Lab.png")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the background image
    screen.blit(background_image, (0, 0))  # (0, 0) is the top-left corner
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
