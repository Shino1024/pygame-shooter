from enum import Enum


class Grades(Enum):
    A, \
    B, \
    C, \
    D, \
    E, \
    F, \
    = range(6)


class PointsSources(Enum):
    """
        Defines where points could be gathered from.
    """
    pass


class PointCalculator:
    """
        Provides basic algorithms for points calculation. It requires that threshold properties (from LevelSettings)
        are provided beforehand. It needs
    """

    __points_
