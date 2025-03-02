from settings import *

class UI:
    def __init__(self, monster):
        self.window = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 36)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50

    def general(self):
        rect  = pygame.Rect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(self.window, COLORS['black'], rect, 0, 4)
        pygame.draw.rect(self.window, COLORS['black'], rect, 4, 4)
        
    def draw(self):
        self.general()
        # Draw health bar
        pygame.draw.rect(self.window, COLORS['black'], (self.left, self.top, 200, 30))
        pygame.draw.rect(self.window, COLORS['red'], (self.left, self.top, 200 * self.monster.health / self.monster.max_health, 30))
        # Draw text
        text = self.font.render(f"{self.monster.name} - {self.monster.health} / {self.monster.max_health}", True, COLORS['white'])
        self.window.blit(text, (self.left, self.top - 40))
        # Draw abilities
        for i, ability in enumerate(self.monster.abilitites):
            text = self.font.render(ability, True, COLORS['white'])
            self.window.blit(text, (self.left, self.top + 40 * i))
        # Draw element
        text = self.font.render(self.monster.element, True, COLORS['white'])
        self.window.blit(text, (self.left, self.top + 40 * (i + 1)))