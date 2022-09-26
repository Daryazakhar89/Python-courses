import pygame

pygame.font.init()


class RegulateSpeed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 50
        self.image = self.get_font_image()
        self.rect = self.image.get_rect()
        self.set_position()

    def get_font_image(self):
        return pygame.font.SysFont("arial", 30).render(f"Speed: {self.speed}", False, (0, 0, 150))

    def set_position(self, position=(0, 0)):
        self.rect.x = position[0]
        self.rect.y = position[1]

    def handle_key_press(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.speed += 1
        if key[pygame.K_DOWN]:
            self.speed -= 1

    def validate_speed(self):
        if self.speed < 0:
            self.speed = 0
        if self.speed > 100:
            self.speed = 100

    def update_speed(self):
        self.image = self.get_font_image()

    def get_speed(self):
        return self.speed

    def update(self):
        self.handle_key_press()
        self.validate_speed()
        self.update_speed()
