from abc import ABCMeta, abstractmethod


class Reactable(metaclass=ABCMeta):
    """
        Classes inheriting from this one are capable of reacting to events.
    """

    @abstractmethod
    def handle_event(self, event):
        pass
