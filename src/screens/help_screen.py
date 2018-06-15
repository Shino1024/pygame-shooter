from src.graphics.gui import Caption, Button
from src.screens.generic_screen import GenericScreen
from src.utilities import system_settings
from src.utilities.asset_manager import AssetManager


class HelpScreen(GenericScreen):
    """
        This screen displays all necessary information to play the game.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Help"
        self.__widgets["screen_caption"] = Caption(self.__screen_text)
        self.__widgets["screen_caption"].y = 20
        self.__widgets["screen_caption"].set_font_name("Caption")
        self.__widgets["screen_caption"].set_font_size(32)
        self.__widgets["screen_caption"].center()

        self.__help_text = (
            "Defeat all enemies and collect as many\n"
            "stars as possible.\n"
            "Use as little time as possible.\n"
            "\n"
            "Use arrows to move.\n"
            "Press 1 to set a bomb.\n"
            "Press 2 to shoot.\n"
        )
        self.__widgets["manual"] = Caption(self.__help_text)
        self.__widgets["manual"].x = 30
        self.__widgets["manual"].y = 50
        self.__widgets["manual"].set_font_name("Caption")
        self.__widgets["manual"].set_font_size(16)

        self.__widgets["back_button"] = Button()
        self.__widgets["back_button"].set_background_color
        self.__widgets["back_button"].w = 40
        self.__widgets["back_button"].h = 30
        offset = 20
        self.__widgets["back_button"].x = system_settings.RESOLUTION_X - self.__widgets["back_button"].w - offset
        self.__widgets["back_button"].y = system_settings.RESOLUTION_Y - self.__widgets["back_button"].h - offset
        button_caption = Caption("Back")
        button_caption.set_font_name("Caption")
        button_caption.set_font_size(18)
        button_caption
        self.__widgets["back_button"].set_caption(button_caption)

    def __render_screen(self, surface):
        self.display_widgets(surface)

    def __load_assets(self):
        AssetManager.load_font("Caption", "example.ttf")
        AssetManager.load_image("Background", "background.png")

    def __finalize(self):
        pass

    def __display_help(self):
        pass
