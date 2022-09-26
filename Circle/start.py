import pygame
import sys

from Circle import Circle
from regulate_speed import RegulateSpeed
from regulate_angle import RegulateAngle


window = pygame.display.set_mode((750, 420))
pygame.display.set_caption("Launch the ball")
background_image = pygame.image.load("moon.png").convert_alpha()
clock = pygame.time.Clock()
fps = 60


player_circle = Circle((255, 0, 255), 25, 45, 45)
speed_regulator = RegulateSpeed()
angle_regulator = RegulateAngle()
all_sprites = pygame.sprite.Group()
all_sprites.add(
    player_circle,
    speed_regulator,
    angle_regulator
)


while True:
    window.blit(background_image, (0, 0))
    all_sprites.update()
    all_sprites.draw(window)

    player_circle.set_initial_speed(speed_regulator.get_speed())
    player_circle.set_initial_angle(angle_regulator.get_angle())

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()

    clock.tick(fps)
