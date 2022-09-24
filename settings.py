import json


class Settings:
    settings = None

    def __init__(self):
        with open("./settings.json", "r") as file_object:
            self.settings = json.load(file_object)

    def get_settings(self):
        return self.settings

    def get_screen(self):
        return self.settings.get("SCREEN")

    def get_color(self, color):
        return self.settings["COLORS"][color]

    def get_heroes(self):
        return self.settings["HEROES"]
