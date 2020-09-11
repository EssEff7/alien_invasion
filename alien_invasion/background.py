import pygame
from pygame.sprite import Sprite

class BackgroundImages(pygame.sprite.Sprite):
    """A class for loading and preparing images to display as background."""
    
    def __init__(self, image_file, location):
        """Load images and get rects."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.background_image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.background_image.get_rect()
        self.rect.left, self.rect.top = location
        
    