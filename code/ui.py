import pygame
from settings import *

class UI:
    def __init__(self, monster, data):
        self.data = data
        self.window = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 36)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster

        # Controls
        self.general_options = ['fight', 'studemon', 'switch', 'run']
        self.general_index = {'col': 0, 'row': 0}
        self.state = 'general'

        # Store button rects for mouse interaction
        self.general_buttons = []
        pygame.key.set_repeat(0)  # Disable key repeat to avoid multiple events


    def input(self):
        """Handle mouse clicks and keyboard input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if self.state == 'general':
                    for i, rect in enumerate(self.general_buttons):
                        if rect.collidepoint(mouse_x, mouse_y):  # Check if clicked inside button
                            if self.general_options[i] == 'fight':
                                self.state = 'textbox'  # Switch to textbox state
                            else:
                                print(f"Selected: {self.general_options[i]}")  # Debugging

            # Process the Enter key only once
            elif event.type == pygame.KEYDOWN:
                if self.state == 'textbox' and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    print("Enter pressed! Changing state to 'general'")  # Debugging
                    self.state = 'general'  # Return to general menu
                    pygame.time.delay(100)
                    # Prevent multiple Enter key detections
                    pygame.event.clear(pygame.KEYDOWN)  # Only remove excess KEYDOWN events


    def draw_textbox(self, message):
        """Draws a text box at the bottom of the screen."""
        box_rect = pygame.Rect(50, WINDOW_HEIGHT - 150, WINDOW_WIDTH - 100, 100)
        pygame.draw.rect(self.window, COLORS['white'], box_rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['black'], box_rect, 4, 4)

        text_surf = self.font.render(message, True, COLORS['black'])
        text_rect = text_surf.get_rect(center=box_rect.center)
        self.window.blit(text_surf, text_rect)

    def quad_select(self, index, options, button_list):
        """Draws a selection box and stores button positions with hover effect."""
        rect = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.window, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['gray'], rect, 4, 4)

        button_list.clear()  # Clear previous button rects
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position

        # Menu options (2x2 grid)
        cols, rows = 2, 2
        for col in range(cols):
            for row in range(rows):
                x = rect.left + rect.width / 4 + (rect.width / 2) * col
                y = rect.top + rect.height / 4 + (rect.height / 2) * row
                i = col + 2 * row  # Calculate index in the list
                
                if i < len(options):
                    text_surf = self.font.render(options[i], True, COLORS['black'])
                    text_rect = text_surf.get_rect(center=(x, y))

                    # Store button rect for mouse detection
                    button_list.append(text_rect.inflate(100, 100))  # Make clickable area slightly bigger

                    # Check if mouse is hovering over this button
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        text_surf = self.font.render(options[i], True, COLORS['gray'])  # Change color if hovered

                    # Draw text
                    self.window.blit(text_surf, text_rect)

    def update(self):
        self.input()

    def draw(self):
        """Draw UI elements based on the current state."""
        if self.state == 'general':
            self.quad_select(self.general_index, self.general_options, self.general_buttons)
        elif self.state == 'textbox':
            self.draw_textbox(f"{self.monster.name} is preparing to attack!")
