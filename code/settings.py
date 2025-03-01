import pygame
from os.path import join
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': 'gray',
    'white': '#ffffff',
}

MONSTER_DATA = {
    'Frone':    {'element': 'fire', 'health': 70},
    'Frubber':   {'element': 'fire', 'health': 150},
    'Intiggy':    {'element': 'water', 'health': 70},
    'Infinibrawl':   {'element': 'water', 'health': 180},
    'Nod':    {'element': 'grass', 'health': 70},
    'Nodree': {'element': 'grass', 'health': 250},
}

ABILITIES_DATA = {
  	'scratch': {'damage': 20,  'element': 'normal', 'animation': 'scratch'},
    'fireball':   {'damage': 35,  'element': 'fire',   'animation': 'fire'},
    'nuke':    {'damage': 50,  'element': 'fire',   'animation': 'explosion'},
    'splash':  {'damage': 30,  'element': 'water',  'animation': 'splash'},
    'shards':  {'damage': 50,  'element': 'water',  'animation': 'ice'},
    'knot':  {'damage': 40,  'element': 'grass',  'animation': 'green'},
}

ELEMENT_DATA = {
    'fire':   {'water': 0.5, 'grass': 2,   'fire': 1,   'normal': 1},
    'water':  {'water': 1,   'grass': 0.5, 'fire': 2,   'normal': 1},
    'grass':  {'water': 2,   'grass': 1,   'fire': 0.5, 'normal': 1},
    'normal': {'water': 1,   'grass': 1,   'fire': 1,   'normal': 1},
}