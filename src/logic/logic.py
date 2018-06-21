import pygame

from src.logic.window import Window
from src.screens.exit_screen import ExitScreen
from src.screens.main_menu_screen import MainMenuScreen
from src.screens.start_screen import StartScreen
from src.utilities import system_settings
from utilities.asset_manager import AssetManager


class ScreenCommander:
    """
        This class is a backbone of the game. It provides a setup and allows to run the game in loop,
        switching between screens.
    """

    __GAME_CLOCK = pygame.time.Clock()

    __current_screen = None

    __SCREEN_STACK = []

    @classmethod
    def setup(cls):
        cls.__prepare_screen(StartScreen)
        Window.start()
        cls.__setup_base_assets()

    @classmethod
    def __setup_base_assets(cls):
        for _, font in system_settings.fonts.items():
            AssetManager.load_asset(font)
            print("loaded")
            print(font)

    @classmethod
    def __fade_out(cls):
        cls.__current_screen.is_fading_out = True
        while cls.__current_screen.is_fading_out:
            cls.__update()

    @classmethod
    def __fade_in(cls):
        cls.__current_screen.is_fading_in = True
        while cls.__current_screen.is_fading_in:
            cls.__update()

    @classmethod
    def run(cls):
        while True:
            if cls.__current_screen.has_finished:
                cls.__fade_out()
                print("ahem")
                if type(cls.__current_screen) == ExitScreen:
                    cls.quit()
                elif len(cls.__SCREEN_STACK) == 0:
                    print("CREATING FIRST")
                    cls.__current_screen = MainMenuScreen()
                else:
                    cls.__current_screen = cls.__SCREEN_STACK.pop()
                cls.__fade_in()

            elif cls.__current_screen.has_advanced:
                cls.__fade_out()
                cls.__current_screen.has_advanced = False
                next_screen = cls.__current_screen.get_next_screen()
                remaining_data = cls.__current_screen.return_data()
                cls.__current_screen.clear_data()

                cls.__SCREEN_STACK.append(cls.__current_screen)
                cls.__prepare_screen(next_screen(**remaining_data))
                cls.__fade_in()

            cls.__update()

    @classmethod
    def __event_passthrough(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Window.exit()
            else:
                cls.__current_screen.handle_event(event)

    @classmethod
    def __update(cls):
        cls.__event_passthrough()
        cls.__current_screen.render(Window.get_surface())
        Window.update()
        cls.__GAME_CLOCK.tick(system_settings.FRAMES_PER_SECOND)

    @classmethod
    def __prepare_screen(cls, screen):
        cls.__current_screen = screen()
        cls.__current_screen.setup_assets()
        cls.__current_screen.load_assets()

    @staticmethod
    def quit():
        Window.exit()
