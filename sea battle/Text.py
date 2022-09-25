import pygame


class TextOutput(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()
        self.image = pygame.font.SysFont("arial", 100).render(text, True, (255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 250
