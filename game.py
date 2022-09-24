import pygame
import sys
import random

from monsters import Monster
from settings import Settings
from cart import Cart
from CollisionHandler import CollisionHandler
from ScoreCounter import ScoreCounter
from TextHandler import TextHandler
from lives import Lives


pygame.init()
pygame.time.set_timer(pygame.USEREVENT, random.randint(1500, 2500))
settings = Settings().get_settings()

windows = pygame.display.set_mode((settings["SCREEN"]["WIDTH"], settings["SCREEN"]["HEIGHT"]))
background = pygame.image.load("assets/image/background.jpg")
pygame.display.set_caption("Сatch the monster")
pygame.display.set_icon(pygame.image.load("assets/image/icon.jpg"))
pygame.mixer.music.load("assets/audio/game_music.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

cart = Cart()
heroes_group = pygame.sprite.Group()
texts_group = pygame.sprite.Group()
text_handler = TextHandler(texts_group)
score_counter = ScoreCounter(text_handler)
collision_handler = CollisionHandler(score_counter)
lives = Lives(text_handler, settings, 5)


while True:
    clock.tick(settings["GAME"]["FPS"])

    windows.blit(background, (0, 0))

    if lives.get_lives() > 0:
        collision_handler.handle_collision_monster_and_cart(heroes_group, cart)
        heroes_group.draw(windows)
        heroes_group.update()
        lives.check_and_subtract_lives(heroes_group)

    cart.listen_keys()
    cart.check_boundaries()

    windows.blit(cart.image, (cart.rect.x, cart.rect.y))

    texts_group.draw(windows)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            Monster(heroes_group)

    pygame.display.update()