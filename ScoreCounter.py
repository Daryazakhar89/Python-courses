class ScoreCounter:
    def __init__(self, text_handler):
        self._score = 0
        self._text_handler = text_handler
        self.show_score()

    def increment_score(self):
        self._score += 1
        self.show_score()

    def show_score(self):
        self._text_handler.show_text(f"SCORE : {self.get_score()}", 25, 5, 5, "red")

    def get_score(self):
        return self._score
