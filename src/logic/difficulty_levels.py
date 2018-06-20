from enum import Enum


class DifficultyLevels(Enum):
    """
        All available levels. They add up to bonuses.
    """

    EASY, \
        NORMAL, \
        HARD, \
        = range(3)