import pygame.sprite
import random

from settings import Settings


class Monster(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()
        self.settings = Settings()
        self.monster = random.choice(self.settings.get_heroes())
        self.image = pygame.image.load("assets/image/monster.png").convert_alpha()
        self.rect = self.image.get_rect()
        group.add(self)
        self.set_monster()
        self.rect.y = 0
        self.rect.x = random.randrange(0, self.settings.get_screen()["WIDTH"] - self.monster.get("width"))
        self.speed = random.randrange(1, 3)

    def set_monster(self):
        scale = 0.6

        monster = pygame.Surface((self.monster.get("width"), self.monster.get("height")))
        monster.blit(self.image, (0, 0), (
            self.monster.get("x"),
            self.monster.get("y"),
            self.monster.get("width"),
            self.monster.get("height")
        ))
        monster.set_colorkey(self.settings.get_color("BLUE"))
        monster = pygame.transform.scale(monster, (self.monster.get("width") * scale, self.monster.get("height") * scale))
        self.image = monster
        self.rect = self.image.get_rect()

    def move_down(self):
        if self.rect.y < self.settings.get_screen()["HEIGHT"]:
            self.rect.y += self.speed

    def update(self):
        self.move_down()
        if self.rect.y > self.settings.get_screen()["HEIGHT"]:
            self.kill()



