import pygame
from Image import Image


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, x, y, pirate_ship_height):
        super().__init__()
        self.image = Image("assets/img/shot.png").get_sprite_shot(0, 0, 90, 90, 0.2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.pirate_ship_height = pirate_ship_height

    def update(self):
        if self.rect.y > 0:
            self.rect.y += -1 * self.speed
        else:
            self.kill()