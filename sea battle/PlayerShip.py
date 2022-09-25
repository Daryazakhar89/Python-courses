import pygame

from Ship import Ship
from Torpedo import Torpedo


class PlayerShip(Ship):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 3
        self.move_direction = 0
        self.set_ship_in_the_middle()
        self.torpedo_launch_interval_fps = 120
        self.fps_from_torpedo_launched = self.torpedo_launch_interval_fps
        self.sound_1 = pygame.mixer.Sound("assets/audio/gromkiy-moschnyiy-vyistrel-pushki.mp3")

    def set_group(self, group):
        self.group = group

    def set_ship_in_the_middle(self):
        self.y_pos = self.get_screen_interface().get_height() - self.get_ship().get_height()
        x_middle_pos = self.get_screen_interface().get_width() / 2 - self.get_ship().get_width() / 2
        self.move(x_middle_pos, self.y_pos)

    def listen_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.move_direction = -1
        elif key[pygame.K_RIGHT]:
             self.move_direction = 1
        elif key[pygame.K_SPACE]:
            self.fire()
            self.sound_1.play()
            self.fps_from_torpedo_launched -= 1
        else:
            self.move_direction = 0

    def handle_screen_collision(self):
        if self.get_position().x == 0 and self.move_direction == -1:
            self.move_direction = 0
        if self.get_position().right == self.get_screen_interface().get_width() and self.move_direction == 1:
            self.move_direction = 0

    def run(self):
        self.listen_keys()
        self.handle_screen_collision()
        
        self.move(self.move_direction, 0, self.speed)
        
        if (self.fps_from_torpedo_launched < self.torpedo_launch_interval_fps):
            self.fps_from_torpedo_launched -= 1
        if (self.fps_from_torpedo_launched <= 0):
            self.fps_from_torpedo_launched = self.torpedo_launch_interval_fps

    def fire(self):
        if self.fps_from_torpedo_launched == self.torpedo_launch_interval_fps:
            self.torpedo = Torpedo(
                self.get_position().x,
                self.get_position().y, 
                self.get_ship().get_height()
            )
            self.group.add(self.torpedo)

