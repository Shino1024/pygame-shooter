from src.screens.generic_screen import GenericScreen


class GameScreen(GenericScreen):
    """
        The screen of the actual game.
    """

    def render_screen(self, surface):
        pass

    def setup_assets(self):
        pass

    def __del__(self):
        self.finalize()
        super().__del__()

    def finalize(self):
        pass

    def load_map(self):
        pass

    def pause_game(self):
        pass

    def resume_game(self):
        pass

    def display_score(self):
        pass

    def calculate_score(self):
        pass

