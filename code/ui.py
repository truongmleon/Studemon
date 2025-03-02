from settings import *

class UI:
    def __init__(self, monster):
        self.window = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 36)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster
        
        # controls
        self.general_options = ['fight', 'studemon', 'switch', 'run']
        self.general_index = {'col': 0, 'row': 0}
        self.attack_index = {'col': 0, 'row': 0}
        self.state = 'general'
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if self.state == 'general':
            # Temporary variables to update movement
            new_col = self.general_index['col'] + int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
            new_row = self.general_index['row'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

            # Prevent going out of bounds (valid range: 0 to 1)
            self.general_index['col'] = max(0, min(1, new_col))
            self.general_index['row'] = max(0, min(1, new_row))
            if keys[pygame.K_SPACE]:
                self.state = self.general_options[self.general_index['col'] + self.general_index['row'] * 2]
                
        elif self.state == 'attack':
            # Temporary variables to update movement
            new_col = self.attack_index['col'] + int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
            new_row = self.attack_index['row'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

            # Prevent going out of bounds (valid range: 0 to 1)
            self.general_index['col'] = max(0, min(1, new_col))
            self.general_index['row'] = max(0, min(1, new_row))
            if keys[pygame.K_SPACE]:
                self.state = self.general_options[self.general_index['col'] + self.general_index['row'] * 2]
                
                
    def quad_select(self, index, options):
        rect = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.window, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['gray'], rect, 4, 4)
        
        # Menu options (2x2 grid)
        cols, rows = 2, 2
        for col in range(cols):
            for row in range(rows):
                x = rect.left + rect.width / 4 + (rect.width / 2) * col
                y = rect.top + rect.height / 4 + (rect.height / 2) * row
                i = col + 2 * row  # Calculate index in the list

                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']  
                
                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_rect(center=(x, y))
                self.window.blit(text_surf, text_rect)
                
    def update(self):
        self.input()
        
    def draw(self):
        match self.state:
            case 'general': self.quad_select(self.general_index, self.general_options)
            case 'attack': self.quad_select(self.attack_index, self.monster.abilities)
        
