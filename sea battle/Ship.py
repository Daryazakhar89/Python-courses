import pygame
from Image import Image


class Ship:
    def __init__(self, sprite_path, screen_interface):
        self._image = Image(sprite_path)
        self.ship_left = self._image.get_image(0, 0, 180, 160, 0.6)
        self.ship_right = pygame.transform.flip(self.ship_left.copy(), True, False)

        self._screen_interface = screen_interface
        self.direction = pygame.math.Vector2()
        self.ship = self.ship_left
        self._rect = self.ship_left.get_rect()

    def move(self, x, y, speed=1):
        if self.direction.x < 0:
            self.ship = self.ship_left
        elif self.direction.x > 0:
            self.ship = self.ship_right

        self.direction.x = x
        self.direction.y = y
        self._rect.center += self.direction * speed

    def get_position(self):
        return self._rect

    def get_ship(self):
        return self.ship

    def get_screen_interface(self):
        return self._screen_interface