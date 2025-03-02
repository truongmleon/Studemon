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

        # Input text box variables
        self.input_text = ""
        self.active = False
        self.max_chars = 30  # Maximum characters in input box
        
        # Display text box variables
        self.display_text = f"{self.monster.name} is preparing to attack!"
        self.display_text_lines = []  # For multi-line text


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
                                self.active = True  # Activate text input
                            else:
                                print(f"Selected: {self.general_options[i]}")  # Debugging
                
                elif self.state == 'textbox':  # Check if clicking in text box
                    box_rect = pygame.Rect(50, WINDOW_HEIGHT - 150, WINDOW_WIDTH - 100, 100)
                    if box_rect.collidepoint(mouse_x, mouse_y):
                        self.active = True  # Activate the input box
                    else:
                        # If they click outside the box but inside textbox state, submit input
                        print(f"Input submitted: {self.input_text}")
                        self.active = False
                        # Optionally reset input text or return to general menu
                        # self.input_text = ""
                        # self.state = 'general'

            # Process keyboard input for the text box
            elif event.type == pygame.KEYDOWN:
                if self.state == 'textbox':
                    if event.key == pygame.K_RETURN:
                        print(f"Input submitted: {self.input_text}")
                        # Process the input (example: update display text based on input)
                        if self.input_text:
                            self.set_display_text(f"You entered: {self.input_text}")
                            self.input_text = ""  # Clear input after submission
                        self.active = True  # Keep text box active for further input
                        pygame.time.delay(100)
                        pygame.event.clear(pygame.KEYDOWN)  # Clear excess KEYDOWN events
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]  # Remove last character
                    elif event.key == pygame.K_ESCAPE:
                        self.active = False
                        self.state = 'general'  # Cancel and return to general menu
                    else:
                        # Add character if not at max length
                        if len(self.input_text) < self.max_chars:
                            self.input_text += event.unicode


    def draw_display_box(self):
        """Draws a large text box for displaying game messages above the input box."""
        # Position the display box above the input box
        box_rect = pygame.Rect(50, WINDOW_HEIGHT - 300, WINDOW_WIDTH - 100, 130)
        
        # Draw display box
        pygame.draw.rect(self.window, COLORS['white'], box_rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['black'], box_rect, 4, 4)
        
        # Format text to fit within box (simple word wrap)
        if not self.display_text_lines:
            self._wrap_text(self.display_text, box_rect.width - 40)
            
        # Draw each line of text
        for i, line in enumerate(self.display_text_lines):
            text_surf = self.font.render(line, True, COLORS['black'])
            text_rect = text_surf.get_rect(topleft=(box_rect.left + 20, box_rect.top + 20 + i * 40))
            self.window.blit(text_surf, text_rect)
    
    def _wrap_text(self, text, max_width):
        """Breaks text into lines that fit within the given width."""
        self.display_text_lines = []
        words = text.split(' ')
        current_line = words[0]
        
        for word in words[1:]:
            # Test width with new word added
            test_line = current_line + ' ' + word
            test_surf = self.font.render(test_line, True, COLORS['black'])
            
            if test_surf.get_width() <= max_width:
                current_line = test_line  # Word fits, add it to current line
            else:
                self.display_text_lines.append(current_line)  # Line is full, store it
                current_line = word  # Start a new line with the word
        
        # Don't forget to add the last line
        if current_line:
            self.display_text_lines.append(current_line)
    
    def set_display_text(self, new_text):
        """Updates the text shown in the display box."""
        self.display_text = new_text
        self.display_text_lines = []  # Clear cached lines to force re-wrap
            
    def draw_input_box(self):
        """Draws an input text box at the bottom of the screen."""
        box_rect = pygame.Rect(50, WINDOW_HEIGHT - 150, WINDOW_WIDTH - 100, 100)
        
        # Box background color changes when active
        bg_color = COLORS['white']
        if self.active:
            bg_color = (220, 220, 255)  # Light blue when active
            
        pygame.draw.rect(self.window, bg_color, box_rect, 0, 4)
        
        # Border color changes when active
        border_color = COLORS['gray'] if self.active else COLORS['black']
        pygame.draw.rect(self.window, border_color, box_rect, 4, 4)

        # Draw the input text
        text_surf = self.font.render(self.input_text, True, COLORS['black'])
        text_rect = text_surf.get_rect(midleft=(box_rect.left + 20, box_rect.centery))
        self.window.blit(text_surf, text_rect)
        
        # Draw blinking cursor when active
        if self.active and pygame.time.get_ticks() % 1000 < 500:  # Blink every half second
            cursor_x = text_rect.right + 2
            cursor_y = text_rect.top
            cursor_height = text_rect.height
            pygame.draw.line(self.window, COLORS['black'], 
                            (cursor_x, cursor_y), 
                            (cursor_x, cursor_y + cursor_height), 
                            2)

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
            self.draw_display_box()  # Draw the display text box first
            self.draw_input_box()    # Then draw the input box below it