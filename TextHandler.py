import pygame.font
import pygame


class TextHandler(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self._group = group

    def show_text(self, text, font_size, x, y, color):
        font = pygame.font.SysFont("Arial", font_size, bold=True)
        self.image = font.render(text, True, pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._group.add(self)

        return self



