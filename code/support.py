from settings import * 
import pygame
import os

"""
Loads all images from a specified folder and returns a dictionary of surfaces.

Args:
    *path: A variable-length argument list representing folder paths.

Returns:
    A dictionary where keys are file names (without extensions) 
    and values are Pygame surfaces (image objects).
"""

def folder_importer(*path):
    surfs = {}
    
    # walk through the folder and get all the files
    for folder_path, _, file_name in walk(join(*path)):
        # load all the images
        for file_name in file_name:
            full_path = join(folder_path, file_name)
            surfs[file_name.split('.')[0]] = pygame.image.load(full_path).convert_alpha()
    return surfs

def audio_importer(*path):
    sounds = {}
    for folder_path, _, file_name in walk(join(*path)):
        for file_name in file_name:
            sounds[file_name.split('.')[0]] = pygame.mixer.Sound(join(folder_path, file_name))
    return sounds
