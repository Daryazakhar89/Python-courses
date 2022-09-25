import pygame


class Explosion(pygame.sprite.Sprite):
    WIDTH = 60
    HEIGHT = 60

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load("assets/img/burst.png")
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.counter = 0

    def set_explosion_coords(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        animation_frames = 10
        pygame.time.Clock().tick(animation_frames)
        self.image = self.get_frame(self.counter, 1.5)

        self.counter += 1

        if self.counter == animation_frames:
            self.counter = 0

    def get_frame(self, number, scale):
        x_mult = number % 3
        y_mult = number // 3
        x = 50 + (x_mult * 160)
        y = 50 + (y_mult * 160)
        surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        surface.blit(self.sprite_sheet, (0, 0), (x, y, self.WIDTH, self.HEIGHT))
        surface.set_colorkey((0, 0, 0))
        surface = pygame.transform.scale(surface, (self.WIDTH * scale, self.HEIGHT * scale))

        return surface


