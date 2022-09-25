import pygame
from Ship import Ship
from Explosion import Explosion
from Text import TextOutput
from Torpedo import Torpedo


class PirateShip(Ship):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 1
        self.speed_increment = 1.1
        self.move_direction = 1
        self.max_speed = 10
        self.torpedo = None
        self.sink = False
        self.sound_2 = pygame.mixer.Sound("assets/audio/vzryiv-v-vode-32129.ogg")

    def set_group(self, group):
        self.group = group

    def increase_speed(self):
        self.speed = self.speed * self.speed_increment
        self.speed = self.speed if self.speed < self.max_speed else self.max_speed

    def run(self):
        current_position = self.get_position()
        if current_position.x > self.get_screen_interface().get_width() - self.get_ship().get_width():
            self.move_direction = -1
            self.increase_speed()
        elif current_position.x < 0:
            self.move_direction = 1
            self.increase_speed()

        if self.sink:
            self.move_direction = 0

        self.move(self.move_direction, 0, self.speed)
        self.check_torpedo_collide()

    def check_torpedo_collide(self):     
        torpedoes = []
        
        if len(self.group.spritedict):
            torpedoes = [sprite for sprite in self.group.spritedict if type(sprite) is Torpedo]

        if len(torpedoes):
            torpedo_list = list(filter(lambda torpedo: self.get_position().colliderect(torpedo.rect), torpedoes))
            if len(torpedo_list):
                x = torpedo_list[0].rect.x
                self.show_explosion(x, self.get_position().centery)
                torpedo_list[0].kill()
                self.sound_2.play()
                self.sink = True
                self.group.add(TextOutput("You win!!!"))
                pygame.time.set_timer(pygame.QUIT, 5000)

    def show_explosion(self, x, y):
        explosion = Explosion()
        explosion.set_explosion_coords(x, y)
        self.group.add(explosion)