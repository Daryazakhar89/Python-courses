import pygame.mixer


class Lives:
    def __init__(self, text_handler, settings, lives):
        self.lives = lives
        self.settings = settings
        self._text_handler = text_handler
        self.sound_game_over = pygame.mixer.Sound("assets/audio/sound_game_over.mp3")

    def check_and_subtract_lives(self, monster_group):
        for monster in monster_group.sprites():
            if monster.rect.bottom >= self.settings["SCREEN"].get("HEIGHT"):
                self.lives -= 1
                monster.kill()
            if self.lives <= 0:
                self._text_handler.show_text("GAME OVER!!!", 50, 180, 125, "black")
                self.sound_game_over.play()
                pygame.time.set_timer(pygame.QUIT, 3000)

    def get_lives(self):
        return self.lives
