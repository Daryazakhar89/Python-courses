import pygame
import sys

from PirateShip import PirateShip
from PlayerShip import PlayerShip
from ScreenInterface import ScreenInterface

screen_width = 600
screen_height = 500
fps = 60

pygame.init()
pygame.display.set_caption("Sea battle")
pygame.display.set_icon(pygame.image.load("assets/img/ship.png"))
windows = pygame.display.set_mode((screen_width, screen_height))

screen_interface = ScreenInterface(screen_width, screen_height)
group = pygame.sprite.Group()

pirate_ship = PirateShip("assets/img/ships.png", screen_interface)
player_ship = PlayerShip("assets/img/ships.png", screen_interface)
pirate_ship.set_group(group)
player_ship.set_group(group)
pygame.mixer.music.load("assets/audio/more-slegka-volnuetsya.ogg")
pygame.mixer.music.play()

clock = pygame.time.Clock()
background = pygame.image.load("assets/img/background.jpg")


while True:
    pirate_ship.run()
    player_ship.run()

    windows.blit(background, (0, 0))
    windows.blit(pirate_ship.get_ship(), pirate_ship.get_position())
    windows.blit(player_ship.get_ship(), player_ship.get_position())
    group.draw(windows)
    group.update()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()