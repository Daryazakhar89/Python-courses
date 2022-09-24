import pygame
from settings import Settings


class Cart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/image/cart.png").convert_alpha()
        self.settings = Settings()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.width * 0.5, self.rect.height * 0.5))
        self.image.set_colorkey(self.settings.get_color("WHITE"))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 215
        self.speed = 10

    def listen_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def check_boundaries(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > self.settings.get_screen().get("WIDTH") - self.rect.width:
            self.rect.x = self.settings.get_screen().get("WIDTH") - self.rect.width
