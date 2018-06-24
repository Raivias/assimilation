import abc

from mapobjects.limits import Limits
from mapobjects.location import Location2D
from mapobjects.shape import Shape


class MapObject(abc.ABC):
    def __init__(self, location, shape, limits):
        if not isinstance(location, Location2D):
            raise TypeError("location was not of type Location")
        self.location = location

        if not isinstance(shape, Shape):
            raise TypeError("shape was not of type Shape")
        self.shape = shape

        if not isinstance(limits, Limits):
            raise TypeError("limits was not of type Limits")
        self.limits = limits

    @abc.abstractmethod
    def move(self, current_state):
        raise NotImplemented()
