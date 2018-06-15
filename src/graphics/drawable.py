from abc import abstractmethod, ABCMeta
#
#
# class Transitional:
#     """
#         This class allows to m
#     """
#
#     def fade_in(self, surface, time_length):
#         pass
#
#     def fade_out(self, surface, time_length):
#         pass


class Drawable(metaclass=ABCMeta):
    """
        All objects of that instance allow to draw anything on provided surface.
    """

    @abstractmethod
    def render(self, surface):
        pass
