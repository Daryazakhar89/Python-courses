import pygame


class Image:
    def __init__(self, pathToImage):
        super().__init__()
        self.image = pygame.image.load(pathToImage).convert_alpha()

    def get_image(self, x, y, width, height, scale):
        surface = pygame.Surface((width, height)).convert_alpha()
        surface.blit(self.image, (x, y), (0, 260, width, height))
        surface = pygame.transform.scale(surface, (width * scale, height * scale))
        surface.set_colorkey((0, 0, 0))
        
        return surface

    def get_sprite_shot(self, x, y, width, height, scale):
        surface = pygame.Surface((width, height)).convert_alpha()
        surface.blit(self.image, (x, y), (110, 60, width, height))
        surface = pygame.transform.scale(surface, (width * scale, height * scale))
        surface.set_colorkey((0, 0, 0))
        
        return surface

    def get_explosion(self, x, y, width, height, scale):
        surface = pygame.Surface((width, height)).convert_alpha()
        surface.blit(self.image, (x, y), (210, 210, width, height))
        surface = pygame.transform.scale(surface, (width * scale, height * scale))
        surface.set_colorkey((0, 0, 0))
        
        return surface