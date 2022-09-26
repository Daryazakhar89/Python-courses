import pygame
import math


class Circle(pygame.sprite.Sprite):
    BLACK = (0, 0, 0)
    G = 9.81

    def __init__(self, color, radius, speed, angle=45):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill(Circle.BLACK)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.image.set_colorkey(Circle.BLACK)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.angle = math.radians(angle)
        self.time = 0
        self.is_timer_started = False
        self.direction = 1  # 1 - right; -1 - left
        self.diameter = radius * 2

    @staticmethod
    def get_screen_width():
        return pygame.display.get_window_size()[0]

    @staticmethod
    def get_screen_height():
        return pygame.display.get_window_size()[1]

    @staticmethod
    def get_time_increment():
        speed_multiplier = 5
        return 1 * speed_multiplier / 60

    def set_initial_speed(self, speed):
        if not self.is_timer_started:
            self.speed = speed

    def set_initial_angle(self, angle):
        if not self.is_timer_started:
            self.angle = math.radians(angle)

    def handle_key_press(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.start_timer()

    def set_coordinates(self):
        self.rect.x = self.get_x()
        self.rect.y = self.get_y()

    def start_timer(self):
        self.is_timer_started = True

    def stop_timer(self):
        self.is_timer_started = False
        self.time = 0

    def reset_timer(self):
        self.time = 0

    def revert_direction(self):
        self.direction *= -1

    def update_timer(self):
        if self.is_timer_started:
            self.time += Circle.get_time_increment()

    def get_x(self):
        if self.time == 0:
            return self.rect.x
        else:
            return round(self.rect.x + self.speed * math.cos(self.angle) * Circle.get_time_increment() * self.direction)

    def get_y(self):
        return Circle.get_screen_height() - self.diameter - self.speed * math.sin(self.angle) * self.time \
               + (Circle.G * math.pow(self.time, 2) / 2)

    def check_ball_touch_ground(self, speed):
        if self.rect.y >= Circle.get_screen_height() - self.diameter:
            self.speed = math.floor(speed * 0.7)
            self.reset_timer()

    def check_ball_touch_wall(self):
        if self.rect.x > Circle.get_screen_width() - self.diameter or self.rect.x < 0:
            self.revert_direction()

    def check_if_speed_equal_zero(self):
        if self.speed == 0:
            self.stop_timer()

    def update(self):
        self.handle_key_press()
        self.update_timer()
        self.set_coordinates()
        self.check_ball_touch_ground(self.speed)
        self.check_ball_touch_wall()
        self.check_if_speed_equal_zero()

