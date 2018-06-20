class MapElement:
    def __init__(self, obj):
        self.__field_type = obj["field_type"]
        self.__x = obj["x"]
        self.__y = obj["y"]
        self.__obj = obj


class LevelSettings:
    """
        Provides basic level configuration.
    """

    def __init__(self, obj):
        self.__difficulty = obj["difficulty"]
        self.__time = obj["time"]
        self.__points = obj["points"]

    def get_difficulty(self):
        return self.__difficulty

    def get_time(self):
        return self.__time

    def get_points(self):
        return self.__points


class Map:
    """
        Contains all data associated with the map level.
    """

    __map_data = []

    def __init__(self):
        pass
