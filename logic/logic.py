import pygame

from graphics.window import Window
from screens.start_screen import StartScreen
from utilities import system_settings


class ScreenCommander:
    """
        This class is a backbone of the game. It provides a setup and allows to run the game in loop,
        switching between screens.
    """

    __SCREEN_SURFACE = None

    __game_clock = pygame.time.Clock()

    __window = Window()

    __current_screen = None
    __next_screen = None

    def setup(self):
        pygame.font.init()
        self.__SCREEN_SURFACE = self.__window.start()

    def make_transition_effect(self):
        pass

    def run(self):
        while True:
            if self.__current_screen is None:
                self.__current_screen = StartScreen()

            self.__current_screen.generate_scene(self.__SCREEN_SURFACE)
            if self.__current_screen.is_finished:
                self.__next_screen = self.__current_screen.get_next_screen()

            if self.__next_screen is not None:
                self.make_transition_effect()

            self.__game_clock.tick(system_settings.FRAMES_PER_SECOND)
            pygame.display.flip()

    def quit(self):
        # Display exit screen?

        pygame.quit()


class EventHandling:
    pass
