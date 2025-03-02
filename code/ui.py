from settings import *

class UI:
    def __init__(self, monster):
        self.window = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 36)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster

    def general(self):
        rect  = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.window, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['gray'], rect, 4, 4)
        
    def draw(self):
        self.general()
