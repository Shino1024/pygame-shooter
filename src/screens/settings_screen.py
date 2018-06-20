from src.graphics.colors import Colors
from src.graphics.gui import Button, Caption
from src.screens.generic_screen import GenericScreen
from src.utilities.asset_manager import AssetManager
from src.utilities.asset_util import AssetTypes, AssetInfo
from src.utilities import system_settings


class SettingsScreen(GenericScreen):
    """
        A screen which lets the player change basic game settings.
    """

    def __init__(self):
        super().__init__()

        self.__SCREEN__TEXT = "Settings"

        button_begin_offset = 100
        button_offset = 20
        left_offset = 20
        top_button_offset = 80
        top_button_offset_inner = 30

        on_caption = Caption("ON!")
        on_caption.set_font_info(system_settings.fonts[20])
        off_caption = Caption("OFF!")
        off_caption.set_font_info(system_settings.fonts[20])
        back_caption = Caption("Back!")
        back_caption.set_font_info(system_settings.fonts[24])

        self.__background = AssetInfo(AssetTypes.IMAGE, "SSB", "SSB.png")

        self.widgets["screen_text"] = Caption(self.__SCREEN__TEXT)
        self.widgets["screen_text"].set_font_info(system_settings.fonts[32])

        self.widgets["music_caption"] = Caption("Music")
        self.widgets["music_caption"].set_font_info(system_settings.fonts[20])
        self.widgets["music_caption"].x = left_offset
        self.widgets["music_caption"].y = top_button_offset
        self.widgets["music_caption"].set_color(Colors.LIGHT_CYAN)

        self.widgets["music_on"] = Button()
        self.widgets["music_on"].set_caption(on_caption)
        self.widgets["music_on"].auto_size()
        self.widgets["music_on"].x = button_begin_offset
        self.widgets["music_on"].y = top_button_offset

        self.widgets["music_off"] = Button()
        self.widgets["music_off"].set_caption(off_caption)
        self.widgets["music_off"].auto_size()
        self.widgets["music_off"].x = self.widgets["music_on"].x + self.widgets["music_on"].w + button_offset
        self.widgets["music_off"].y = top_button_offset

        self.widgets["sfx_caption"] = Caption("Sound")
        self.widgets["sfx_caption"].set_font_info(system_settings.fonts[20])
        self.widgets["sfx_caption"].x = left_offset
        self.widgets["sfx_caption"].set_color(Colors.LIGHT_CYAN)
        self.widgets["sfx_caption"].y = self.widgets["music_caption"].y + self.widgets["music_caption"].h + top_button_offset_inner

        self.widgets["sfx_on"] = Button()
        self.widgets["sfx_on"].set_caption(on_caption)
        self.widgets["sfx_on"].auto_size()
        self.widgets["sfx_on"].x = 40
        self.widgets["sfx_on"].y = self.widgets["sfx_on"].y + self.widgets["sfx_on"].h + top_button_offset_inner

        self.widgets["sfx_off"] = Button()
        self.widgets["sfx_off"].set_caption(off_caption)
        self.widgets["sfx_off"].auto_size()
        self.widgets["sfx_off"].x = self.widgets["sfx_off"].x + self.widgets["sfx_off"].w + button_offset
        self.widgets["sfx_off"].y = self.widgets["sfx_off"].y + self.widgets["sfx_off"].h + top_button_offset_inner

        self.widgets["back_button"] = Button()
        self.widgets["back_button"].set_caption(back_caption)
        self.widgets["back_button"].set_color(Colors.RED)
        self.widgets["back_button"].auto_size()
        self.widgets["back_button"].x = system_settings.RESOLUTION_X - button_offset - self.widgets["back_button"].w
        self.widgets["back_button"].y = system_settings.RESOLUTION_Y - button_offset - self.widgets["back_button"].h

    def __display_background(self, surface):
        background_image = AssetManager.get_asset(self.assets["background_image"])
        surface.blit(background_image, (0, 0))

    def render_screen(self, surface):
        self.__display_background(surface)
        self.display_widgets(surface)

    def setup_assets(self):
        self.assets["background_image"] = AssetInfo(AssetTypes.IMAGE, "SSBG", "SSBG.png")

    def finalize(self):
        pass

    def __del__(self):
        self.finalize()
        super().__del__()
