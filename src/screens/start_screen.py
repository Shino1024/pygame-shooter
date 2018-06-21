from src.screens.generic_screen import GenericScreen
from src.screens.main_menu_screen import MainMenuScreen
from src.utilities import system_settings
from src.utilities.asset_manager import AssetManager
from utilities.asset_util import AssetTypes, AssetInfo
from src.graphics.colors import Colors


class StartScreen(GenericScreen):
    """
        A welcome screen shown briefly at the beginning of the game.
    """

    def __init__(self):
        super().__init__()

        self.__SECONDS_INTERVAL = 5
        self.__FRAMES_NUM = system_settings.FRAMES_PER_SECOND * self.__SECONDS_INTERVAL
        self.__frames_passed = 0

        self.__next_screen = MainMenuScreen

    def setup_assets(self):
        self.assets["splash"] = AssetInfo(AssetTypes.IMAGE, "splash", "splash.png")
        AssetManager.load_asset(self.assets["splash"])

    def render_screen(self, surface):
        if self.__frames_passed % 50 == 0:
            print(self.__frames_passed)
        if self.__frames_passed == self.__FRAMES_NUM:
            print("finished")
            self.has_finished = True

        # print(self.assets["splash"])
        # coord_x = (system_settings.RESOLUTION_X - AssetManager.get_asset("image", "splash", "splash.png")).x) / 2
        self.__frames_passed += 1
        coord_x = (system_settings.RESOLUTION_X - AssetManager.get_asset(self.assets["splash"]).get_width()) / 2
        coord_y = (system_settings.RESOLUTION_Y - AssetManager.get_asset(self.assets["splash"]).get_height()) / 2
        surface.fill(Colors.WHITE.value)
        surface.blit(AssetManager.get_asset(self.assets["splash"]), (coord_x, coord_y))

    def finalize(self):
        pass

    def __del__(self):
        self.finalize()
        super().__del__()
