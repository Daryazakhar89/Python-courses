import pygame


class CollisionHandler:
    def __init__(self, score_counter):
        self.score_counter = score_counter
        self.sound_catch = pygame.mixer.Sound("assets/audio/catch_sound.mp3")

    def handle_collision_monster_and_cart(self, monster_group, cart):
        for monster in monster_group.sprites():
            is_collide = cart.rect.colliderect(monster)
            if is_collide and CollisionHandler.is_monster_above_cart(monster, cart):
                self.score_counter.increment_score()
                self.sound_catch.play()
                monster.kill()

    @staticmethod
    def is_monster_above_cart(monster, cart):
        return monster.rect.bottom <= cart.rect.top + 2
