import utilities.asset_util
from src.graphics import colors
from src.graphics import gui
from src.logic import level_parser # import LevelParser
from src.screens import generic_screen # import GenericScreen
from src.utilities import asset_manager # import AssetTypes, AssetInfo, AssetManager
from src.utilities import system_settings


class LevelSelectScreen(generic_screen.GenericScreen):
    """
        A screen which displays available levels.
    """

    def __init__(self):
        super().__init__()

        self.__screen_text = "Level select"

        self.__MAX_LEVELS_ONSCREEN = 8
        self.__LEVELS_BUTTONS_OFFSET = 40
        self.__BUTTONS_INNER_OFFSET = 10

        self.__chosen_level_id = None
        level_parser.LevelParser.fetch_levels_names()
        self.__LEVEL_NAMES = level_parser.LevelParser.get_levels_names()

    def setup_assets(self):
        self.assets["background_image"] = utilities.asset_util.AssetInfo(utilities.asset_util.AssetTypes.IMAGE, "LSSBG", "LSSBG.png")

    def render_screen(self, surface):
        self.__display_background(surface)
        self.__get_levels()
        self.display_widgets(surface)

    def __del__(self):
        self.finalize()
        super().__del__()

    def finalize(self):
        pass

    def __display_background(self, surface):
        bg_image = asset_manager.AssetManager.get_asset(self.assets["background_image"])
        surface.blit(bg_image, (0, 0))

    def __get_levels(self):
        levels_names = level_parser.LevelParser.get_levels_names()
        levels_num = min(len(levels_names), self.__MAX_LEVELS_ONSCREEN)
        for i in range(levels_num):
            level_id = "level" + str(i)
            level_button_caption = gui.Caption(levels_names[i])
            level_button_caption.set_font_info(system_settings.fonts[16])
            level_button_caption.set_color(colors.Colors.WHITE)
            self.widgets[level_id] = gui.Button()
            self.widgets[level_id].set_background_color(colors.Colors.GRAY)
            self.widgets[level_id].set_caption(level_button_caption)
            self.widgets[level_id].auto_size()
            self.widgets[level_id].center()
            self.widgets[level_id].y = self.__LEVELS_BUTTONS_OFFSET + i * (self.widgets[level_id].h + self.__BUTTONS_INNER_OFFSET)
