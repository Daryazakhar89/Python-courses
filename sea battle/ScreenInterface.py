class ScreenInterface:
    def __init__(self, screen_width, screen_height):
        self._width = screen_width
        self._height = screen_height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
