from src.screens.generic_screen import GenericScreen
from src.utilities import AssetManager
from src.utilities.asset_manager import AssetTypes


class LevelSelectScreen(GenericScreen):
    """
        A screen which displays available levels.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Level select"

        self.__chosen_level_id = None
        AssetManager

    def __render_screen(self, surface):
        self.__display_background(surface)
        self.__display_widgets(surface)
        self.__display_levels(surface)

    def __finalize(self):
        pass

    def __display_background(self, surface):
        bg_image = AssetManager.get_asset(AssetTypes.IMAGE, self.__screen_text)
        bg_image.render(surface)

    def display_levels(self, surface):
        pass
