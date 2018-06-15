import pygame

from src.logic.window import Window
from src.screens.exit_screen import ExitScreen
from src.screens.main_menu_screen import MainMenuScreen
from src.screens.start_screen import StartScreen
from src.utilities import system_settings


class ScreenCommander:
    """
        This class is a backbone of the game. It provides a setup and allows to run the game in loop,
        switching between screens.
    """

    __GAME_CLOCK = pygame.time.Clock()

    __current_screen = StartScreen()
    __SCREEN_STACK = []

    @staticmethod
    def setup():
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        Window.start()

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
                # cls.__fade_out()
                if len(cls.__SCREEN_STACK) == 0:
                    cls.__current_screen = MainMenuScreen()
                elif type(cls.__current_screen) == ExitScreen:
                    cls.quit()
                else:
                    cls.__current_screen = cls.__SCREEN_STACK.pop()
                # cls.__fade_in()

            elif cls.__current_screen.has_advanced:
                # cls.__fade_out()
                cls.__current_screen.has_advanced = False
                next_screen = cls.__current_screen.get_next_screen()
                remaining_data = cls.__current_screen.return_data()
                next_screen.setup(remaining_data)
                cls.__current_screen.clear_data()

                cls.__SCREEN_STACK.append(cls.__current_screen)
                cls.__current_screen = next_screen
                # cls.__fade_in()

            cls.__update()

    @classmethod
    def __update(cls):
        cls.__current_screen.render(Window.SCREEN_SURFACE)
        pygame.display.flip()
        cls.__GAME_CLOCK.tick(system_settings.FRAMES_PER_SECOND)

    @staticmethod
    def quit():
        # Display exit screen?

        pygame.quit()
