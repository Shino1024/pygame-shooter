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
        self.widgets["ScreenText"] = Caption(self.__SCREEN_TEXT)
        self.widgets["ScreenText"].set_bold()
        self.widgets["ScreenText"].set_font_size(32)
        self.widgets["ScreenText"].set_color(Colors.WHITE)
        self.widgets["ScreenText"].y = 20
        self.widgets["ScreenText"].center()

        font24 = system_settings.fonts[24]
        font20 = system_settings.fonts[20]

        self.widgets["PlayButton"] = Button()
        play_caption = Caption("Play!")
        play_caption.set_bold_style(True)
        play_caption.set_font_info(font24)
        self.widgets["PlayButton"].set_background_color(Colors.LIGHT_YELLOW)
        self.widgets["PlayButton"].set_caption(play_caption)
        self.widgets["PlayButton"].auto_size()
        self.widgets["PlayButton"].center()
        self.widgets["PlayButton"].y = 60
        self.widgets["PlayButton"].set_action(self.__handle_play_button)

        self.widgets["SettingsButton"] = Button()
        settings_caption = Caption("Settings!")
        settings_caption.set_font_info(font20)
        self.widgets["SettingsButton"].set_background_color(Colors.LIGHT_BLUE)
        self.widgets["SettingsButton"].set_caption(settings_caption)
        self.widgets["SettingsButton"].auto_size()
        self.widgets["SettingsButton"].center()
        self.widgets["SettingsButton"].y = self.widgets["PlayButton"].y + self.widgets["PlayButton"].h + self.__BUTTONS_OFFSET
        self.widgets["SettingsButton"].set_action(self.__handle_settings_button)

        self.widgets["HelpButton"] = Button()
        help_caption = Caption("Manual!")
        help_caption.set_font_info(font20)
        self.widgets["HelpButton"].set_background_color(Colors.LIGHT_RED)
        self.widgets["HelpButton"].set_caption(help_caption)
        self.widgets["HelpButton"].auto_size()
        self.widgets["HelpButton"].center()
        self.widgets["HelpButton"].y = self.widgets["SettingsButton"].y + self.widgets["SettingsButton"].h + self.__BUTTONS_OFFSET
        self.widgets["HelpButton"].set_action(self.__handle_help_button)

        self.widgets["QuitButton"] = Button()
        quit_caption = Caption("Quit!")
        help_caption.set_font_info(font20)
        self.widgets["QuitButton"].set_background_color(Colors.LIGHT_YELLOW)
        self.widgets["QuitButton"].set_caption(quit_caption)
        self.widgets["QuitButton"].auto_size()
        self.widgets["QuitButton"].center()
        self.widgets["QuitButton"].y = self.widgets["HelpButton"].y + self.widgets["HelpButton"].h + self.__BUTTONS_OFFSET
        self.widgets["QuitButton"].set_action(self.__handle_quit_button)

    def setup_assets(self):
        self.assets["background_image"] = AssetInfo(AssetTypes.IMAGE, "MMBG", "MMBG.png")
        self.assets["splash"] = AssetInfo(AssetTypes.IMAGE, "Splash", "splash.png")

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
