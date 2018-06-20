from graphics.colors import Colors
from src.graphics.gui import Caption, Button
from src.screens.generic_screen import GenericScreen
from src.utilities import system_settings
from utilities.asset_manager import AssetManager
from utilities.asset_util import AssetTypes, AssetInfo


class HelpScreen(GenericScreen):
    """
        This screen displays all necessary information to play the game.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Help"
        self.widgets["screen_caption"] = Caption(self.__screen_text)
        self.widgets["screen_caption"].y = 20
        self.widgets["screen_caption"].set_font_name("Caption")
        self.widgets["screen_caption"].set_font_size(32)
        self.widgets["screen_caption"].center()

        self.__help_text = (
            "Defeat all enemies and collect as many\n"
            "stars as possible.\n"
            "Use as little time as possible.\n"
            "\n"
            "Use arrows to move.\n"
            "Press 1 to set a bomb.\n"
            "Press 2 to shoot.\n"
        )
        self.widgets["manual"] = Caption(self.__help_text)
        self.widgets["manual"].x = 30
        self.widgets["manual"].y = 70
        self.widgets["manual"].set_font_info(system_settings.fonts[16])
        self.widgets["manual"].set_color(Colors.LIGHT_MAGENTA)

        self.widgets["back_button"] = Button()
        self.widgets["back_button"].set_background_color(Colors.LIGHT_BLUE)
        self.widgets["back_button"].w = 40
        self.widgets["back_button"].h = 30

        back_caption = "Back!"
        button_offset = 20
        self.widgets["back_button"] = Button()
        self.widgets["back_button"].set_caption(back_caption)
        self.widgets["back_button"].set_color(Colors.RED)
        self.widgets["back_button"].auto_size()
        self.widgets["back_button"].x = system_settings.RESOLUTION_X - button_offset - self.widgets["back_button"].w
        self.widgets["back_button"].y = system_settings.RESOLUTION_Y - button_offset - self.widgets["back_button"].h

    def render_screen(self, surface):
        self.__display_background(surface)
        self.display_widgets(surface)
        self.__display_help(surface)

    def __display_background(self, surface):
        bg_image = AssetManager.get_asset(self.assets["background_image"])
        surface.blit(bg_image, (0, 0))

    def setup_assets(self):
        self.assets["background_image"] = AssetInfo(AssetTypes.IMAGE, "HSBG", "HSBG.png")

    def __del__(self):
        self.finalize()
        super().__del__()

    def finalize(self):
        pass

    def __display_help(self, surface):
        pass
