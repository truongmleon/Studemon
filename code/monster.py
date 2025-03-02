import pygame
from settings import *
from random import sample

class Creature:
    def get_data(self, name):
        # stats
        self.element = MONSTER_DATA[name]['element']
        self.health = self.max_health = MONSTER_DATA[name]['health']
        self.name = name

class Monster(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(bottomleft = (100, WINDOW_HEIGHT))
        self.name = name
        self.get_data(name)
        
class Oponent(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(midbottom = (770, 400))
        self.name = name
        self.get_data(name)
