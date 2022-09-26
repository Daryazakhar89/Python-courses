import pygame

pygame.font.init()


class RegulateAngle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.angle = 45
        self.image = self.get_font_image()
        self.rect = self.image.get_rect()
        self.set_position()

    def get_font_image(self):
        return pygame.font.SysFont("arial", 30).render(f"Angle: {self.angle}", False, (0, 0, 150))

    def set_position(self, position=(0, 40)):
        self.rect.x = position[0]
        self.rect.y = position[1]

    def handle_key_press(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.angle += 1
        if key[pygame.K_LEFT]:
            self.angle -= 1

    def validate_angle(self):
        if self.angle < 0:
            self.angle = 0
        if self.angle > 90:
            self.angle = 90

    def update_angle(self):
        self.image = self.get_font_image()

    def get_angle(self):
        return self.angle

    def update(self):
        self.handle_key_press()
        self.validate_angle()
        self.update_angle()
