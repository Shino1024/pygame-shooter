from src.graphics.gui import Caption, Button
from src.screens.exit_screen import ExitScreen
from src.screens.generic_screen import GenericScreen
from src.screens.help_screen import HelpScreen
from src.screens.level_select_screen import LevelSelectScreen
from src.screens.settings_screen import SettingsScreen
from src.utilities.asset_manager import AssetInfo, AssetTypes
from src.utilities.colors import Colors


class MainMenuScreen(GenericScreen):
    """
        Displays the main screen with menu.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Main menu"
        self.__widgets["ScreenText"] = Caption(self.__screen_text)
        self.__widgets["ScreenText"].set_bold()
        self.__widgets["ScreenText"].set_font_size(32)
        self.__widgets["ScreenText"].set_color(Colors.WHITE)
        self.__widgets["ScreenText"].y = 20
        self.__widgets["ScreenText"].center()

        font24 = AssetInfo(AssetTypes.FONT, "DefaultFont24")
        font20 = AssetInfo(AssetTypes.FONT, "DefaultFont20")

        self.__widgets["PlayButton"] = Button()
        play_caption = Caption("Play!")
        play_caption.set_bold_style(True)
        play_caption.set_font_info(font24)
        self.__widgets["PlayButton"].set_background_color(Colors.LIGHT_YELLOW)
        self.__widgets["PlayButton"].set_caption(play_caption)
        self.__widgets["PlayButton"].auto_size()
        self.__widgets["PlayButton"].center()
        self.__widgets["PlayButton"].y = 60
        self.__widgets["PlayButton"].set_action(self.__handle_play_button)

        self.__widgets["SettingsButton"] = Button()
        settings_caption = Caption("Settings!")
        settings_caption.set_font_info(font20)
        self.__widgets["SettingsButton"].set_caption(settings_caption)
        self.__widgets["SettingsButton"].auto_size()
        self.__widgets["SettingsButton"].center()
        self.__widgets["SettingsButton"].y = self.__widgets["PlayButton"].y + self.__widgets["PlayButton"].h + 10
        self.__widgets["SettingsButton"].set_action(self.__handle_settings_button)

        self.__widgets["HelpButton"] = Button()
        help_caption = Caption("Manual!")
        help_caption.set_font_info(font20)
        self.__widgets["HelpButton"].set_caption(help_caption)
        self.__widgets["HelpButton"].auto_size()
        self.__widgets["HelpButton"].center()
        self.__widgets["HelpButton"].y = self.__widgets["SettingsButton"].y + self.__widgets["SettingsButton"].h + 10
        self.__widgets["HelpButton"].set_action(self.__handle_help_button)

        self.__widgets["QuitButton"] = Button()
        quit_caption = Caption("Quit!")
        help_caption.set_font_info(font20)
        self.__widgets["QuitButton"].set_caption(quit_caption)
        self.__widgets["QuitButton"].auto_size()
        self.__widgets["QuitButton"].center()
        self.__widgets["QuitButton"].y = self.__widgets["HelpButton"].y + self.__widgets["HelpButton"].h + 10
        self.__widgets["QuitButton"].set_action(self.__handle_quit_button)

    def __handle_play_button(self):
        self.has_advanced = True
        self.__next_screen = LevelSelectScreen()

    def __handle_settings_button(self):
        self.__has_advanced = True
        self.__next_screen = SettingsScreen()

    def __handle_quit_button(self):
        self.__has_advanced = True
        self.__next_screen = ExitScreen()

    def __handle_help_button(self):
        self.__has_advanced = True
        self.__next_screen = HelpScreen()

    def __render_screen(self, surface):
        pass

    def __finalize(self):
        pass
