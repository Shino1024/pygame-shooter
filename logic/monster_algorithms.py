from abc import abstractmethod, ABCMeta
from enum import Enum
from entities import Sides

class AvailabilityMap(object):
    """
       Contains a set of fields, each field being either free or taken.
    """

    def __init__(self, in_map):
        self.__availability_map = []

class Algorithm(object, metaclass=ABCMeta):
    """
        This class is a base class of all kinds of monster algorithms. It allows to set basic
        information needed for any algorithm to resolve the best way to move around the map.
        All behaviours depend solely on the type of subclass.
    """

    __player_x = -1
    __player_y = -1
    __monster_x = -1
    __monster_y = -1
    __side = Sides.UP

    self.__availability_map = None

    def set_player_position(self, player_x, player_y):
        self.__player_x = player_x
        self.__player_y = player_y

    def set_availability_map(self, availability_map):
        self.__availability_map = availability_map

    def turn(self, side):
        self.__side = side

    @abstractmethod
    def make_move(self):
        raise NotImplementedError


class IdleBehaviour(Algorithm):
    def make_move(self):
        pass


class WanderingBehaviour(Algorithm):
    def make_move(self):
        pass


class AggressiveBehaviour(Algorithm):
    def make_move(self):
        pass


class BehaviourTypes(Enum):
    """
        Defines types of monster behaviour. Each behaviour is assigned to a class.
    """

    IDLE = IdleBehaviour
    WANDERING = WanderingBehaviour
    AGGRESSIVE = AggressiveBehaviour
