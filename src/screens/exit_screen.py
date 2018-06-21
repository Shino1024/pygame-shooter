from src.screens.generic_screen import GenericScreen
from src.utilities import system_settings
from src.utilities.asset_manager import AssetManager
from utilities.asset_util import AssetTypes, AssetInfo
from src.graphics.colors import Colors


class ExitScreen(GenericScreen):
    """
        This screen is shown just for a few seconds before game exit.
    """

    def __init__(self):
        super().__init__()

        self.__SECONDS_INTERVAL = 5
        self.__FRAMES_NUM = system_settings.FRAMES_PER_SECOND * (self.__SECONDS_INTERVAL * 1000)
        self.__frames_passed = 0
        self.assets["Farewell"] = AssetInfo(AssetTypes.IMAGE, "Farewell", "farewell.png")

        self.__next_screen = None

    def render_screen(self, surface):
        if self.__frames_passed == self.__FRAMES_NUM:
            self.has_finished = True

        self.__frames_passed += 1
        coord_x = (system_settings.RESOLUTION_X - AssetManager.get_asset(self.assets["Farewell"]).x) / 2
        coord_y = (system_settings.RESOLUTION_Y - AssetManager.get_asset(self.assets["Farewell"]).y) / 2
        surface.fill(Colors.WHITE)
        surface.blit(AssetManager.get_asset(self.assets["Farewell"]), (coord_x, coord_y))

    def setup_assets(self):
        pass

    def __del__(self):
        self.finalize()
        super().__del__()

    def finalize(self):
        pass
