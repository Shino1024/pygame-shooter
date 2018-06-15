from enum import Enum


class Grades(Enum):
    """
        Marks that can be achieved for winning the map from the best to the worst.
    """

    A, \
        B, \
        C, \
        D, \
        E, \
        F, \
        = range(6)


class PointsSources(Enum):
    """
        Defines where points could be gathered from, as well as their importance (relative to each other).
    """

    HEALTH_LEFT, \
        TIME_LEFT, \
        STARS = 3, 3, 5


class PointCalculator:
    """
        Provides basic algorithms for points calculation. It requires that threshold properties values
        (from LevelSettings) are provided beforehand. It needs
    """

    __points = {}
    __base_values = {}
    __level = None

    def set_level(self, level):
        self.__level = level

    def set_points_for(self, points_source, value):
        if points_source not in PointsSources:
            raise ValueError("Given points source has been undefined.")

        assert(value > 0)

        self.__points[points_source] = value

    def set_base_value(self, points_source, value):
        if points_source not in PointsSources:
            raise ValueError("Given points source has been undefined.")

        assert(value > 0)

        self.__base_values[points_source] = value

    def calculate_max_points(self):
        points_sum = 0
        for source in PointsSources:
            points_sum += self.__base_values[source] * PointsSources[source]

        return points_sum

    def calculate_points(self):
        points_sum = 0
        for source in PointsSources:
            points_sum += self.__points[source] * PointsSources[source]

        return points_sum

    def get_grade(self):
        max_points = self.calculate_max_points()
        points = self.calculate_points()
        percentage = float(points) / float(max_points)
        level_bonus = self.__level.value
        percentage += level_bonus

        for i, grade in zip(range(5, 10), Grades):
            if percentage < i / 10.:
                return grade
