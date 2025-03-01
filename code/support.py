from settings import * 

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
    for folder_path, _, files in walk(join(*path)):
        # load all the images
        for file_name in files:
            full_path = join(folder_path, files)
            surfs[file_name.split('.')[0]] = pygame.image.load(full_path).convert_alpha()
    return surfs

def audio_importer(*path):
    sounds = {}
    for folder_path, _, files in walk(join(*path)):
        for files in files:
            sounds[files.split('.')[0]] = pygame.mixer.Sound(join(folder_path, files))
    return sounds
