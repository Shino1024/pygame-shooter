from screens.generic_screen import GenericScreen
from utilities.asset_manager import AssetManager


class LevelScreen(GenericScreen):
    """
        A screen which displays available levels.
    """

    def __init__(self):
        self.__chosen_level_id = None
        AssetManager

    def setup(self, **kwargs):
        pass

    def return_data(self):
        return self.__chosen_level_id

    def get_next_screen(self):
        return

    def render(self, surface):
        self.display_background(surface)
        self.display_widgets(surface)
        self.display_levels(surface)

    def display_background(self, surface):
        bg_image = self.__assets["bg_image"]
        bg_image.render(surface)

    def display_levels(self, surface):
        pass
