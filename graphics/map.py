from utilities.system_settings import DifficultyLevels

class MapElement:
    def __init__(self, field_type, x, y, obj):
        self.__field_type = field_type
        self.__x = x
        self.__y = y
        self.__obj = obj


class LevelSettings:

    def __init__(self):
        self.__difficulty = DifficultyLevels.EASY
        self.__time = -1
        self.__points = -1

    def set_all(self, difficulty, time, points):
        self.__difficulty = difficulty
        self.__time = time
        self.__points = points

    def get_difficulty(self):
        return self.__difficulty

    def get_time(self):
        return self.__time

    def get_points(self):
        return self.__points


class Map:
    """
        #
    """

    __map_data = []

    def __init__(self):
        pass
