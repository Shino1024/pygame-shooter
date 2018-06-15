from src.graphics.gui import Button, Caption
from src.screens.generic_screen import GenericScreen
from src.utilities.asset_manager import AssetManager


class SettingsScreen(GenericScreen):
    """
        A screen which lets the player change basic game settings.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Settings"

        self.__widgets["sound_on"] = Button()
        self.__widgets["sound_off"] = Button()
        self.__widgets["sound_switch"] = Caption()

        self.__widgets["sound_switch"].center()
        # self.__widgets[""]

        self.__background_name = "Background"

    def __render_screen(self, surface):
        background_image = AssetManager.get_image(self.__background_name)
        surface.blit(background_image, (0, 0))

        self.display_widgets(surface)
