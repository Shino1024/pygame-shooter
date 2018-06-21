from src.graphics.gui import Caption, Button
from src.screens.exit_screen import ExitScreen
from src.screens.generic_screen import GenericScreen
from src.screens.help_screen import HelpScreen
from src.screens.level_select_screen import LevelSelectScreen
from src.screens.settings_screen import SettingsScreen
from src.graphics.colors import Colors
from utilities import system_settings
from utilities.asset_manager import AssetManager
from utilities.asset_util import AssetTypes, AssetInfo


class MainMenuScreen(GenericScreen):
    """
        Displays the main screen with menu.
    """

    def __init__(self):
        super().__init__()

        self.__BUTTONS_OFFSET = 10

        self.__SCREEN_TEXT = "Main menu"
        self.widgets["screen_text"] = Caption(self.__SCREEN_TEXT)
        self.widgets["screen_text"].set_bold(True)
        self.widgets["screen_text"].set_color(Colors.WHITE.value)
        self.widgets["screen_text"].set_font_info(system_settings.fonts[32])
        self.widgets["screen_text"].y = 20
        self.widgets["screen_text"].center()

        font24 = system_settings.fonts[24]
        font20 = system_settings.fonts[20]

        self.widgets["play_button"] = Button()
        play_caption = Caption("Play!")
        play_caption.set_bold(True)
        play_caption.set_font_info(font24)
        play_caption.set_color(Colors.WHITE.value)
        self.widgets["play_button"].set_background_color(Colors.LIGHT_YELLOW.value)
        print(play_caption)
        self.widgets["play_button"].set_caption(play_caption)
        self.widgets["play_button"].auto_size()
        self.widgets["play_button"].center()
        self.widgets["play_button"].y = 60
        self.widgets["play_button"].set_action(self.__handle_play_button)

        self.widgets["settings_button"] = Button()
        settings_caption = Caption("Settings!")
        print("AAAAAAAAAAAA")
        print(font20)
        settings_caption.set_font_info(font20)
        settings_caption.set_color(Colors.WHITE.value)
        self.widgets["settings_button"].set_background_color(Colors.LIGHT_BLUE.value)
        self.widgets["settings_button"].set_caption(settings_caption)
        self.widgets["settings_button"].auto_size()
        self.widgets["settings_button"].center()
        self.widgets["settings_button"].y = self.widgets["play_button"].y + self.widgets["play_button"].h + self.__BUTTONS_OFFSET
        self.widgets["settings_button"].set_action(self.__handle_settings_button)

        self.widgets["help_button"] = Button()
        help_caption = Caption("Manual!")
        help_caption.set_font_info(font20)
        help_caption.set_color(Colors.WHITE.value)
        self.widgets["help_button"].set_background_color(Colors.LIGHT_RED.value)
        self.widgets["help_button"].set_caption(help_caption)
        self.widgets["help_button"].auto_size()
        self.widgets["help_button"].center()
        self.widgets["help_button"].y = self.widgets["settings_button"].y + self.widgets["settings_button"].h + self.__BUTTONS_OFFSET
        self.widgets["help_button"].set_action(self.__handle_help_button)

        self.widgets["quit_button"] = Button()
        quit_caption = Caption("Quit!")
        quit_caption.set_font_info(font20)
        quit_caption.set_color(Colors.WHITE.value)
        self.widgets["quit_button"].set_background_color(Colors.LIGHT_YELLOW.value)
        self.widgets["quit_button"].set_caption(quit_caption)
        self.widgets["quit_button"].auto_size()
        self.widgets["quit_button"].center()
        self.widgets["quit_button"].y = self.widgets["help_button"].y + self.widgets["help_button"].h + self.__BUTTONS_OFFSET
        self.widgets["quit_button"].set_action(self.__handle_quit_button)

    def setup_assets(self):
        self.assets["background_image"] = AssetInfo(AssetTypes.IMAGE, "MMBG", "MMBG.png")
        self.assets["splash"] = AssetInfo(AssetTypes.IMAGE, "splash", "splash.png")

    def __handle_play_button(self):
        self.has_advanced = True
        self.__next_screen = LevelSelectScreen

    def __handle_settings_button(self):
        self.__has_advanced = True
        self.__next_screen = SettingsScreen

    def __handle_quit_button(self):
        self.__has_advanced = True
        self.__next_screen = ExitScreen

    def __handle_help_button(self):
        self.__has_advanced = True
        self.__next_screen = HelpScreen

    def __display_background(self, surface):
        surface.blit(AssetManager.get_asset(self.assets["background_image"]), (0, 0))

    def __display_splash(self, surface):
        offset_x = (system_settings.RESOLUTION_X -
                    AssetManager.get_asset(self.assets["splash"]).get_width()) / 2
        offset_y = 40
        surface.blit(AssetManager.get_asset(self.assets["splash"]), (offset_x, offset_y))

    def render_screen(self, surface):
        self.__display_background(surface)
        self.__display_splash(surface)
        self.display_widgets(surface)

    def __del__(self):
        self.finalize()
        super().__del__()

    def finalize(self):
        pass
