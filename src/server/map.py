import abc


class Map:
    def __init__(self, objects=None):
        if objects is None:
            objects = []
        if not isinstance(objects, list):
            raise TypeError("objects was not list")

        for ob in objects:
            if not isinstance(ob, MapObject):
                raise TypeError("objects contained non-MapObject")

        self.objects = objects
        return

    def add_object(self, ob):
        if not isinstance(ob, MapObject):
            raise TypeError("object was not of type MapObject")
        self.objects.append(ob)
        return True

    def next_state(self):
        obs_1 = []
        for ob in self.objects:
            obs_0 = self.objects.copy()
            obs_1.append(ob.move(obs_0))
        new_map = Map(obs_1)
        return new_map


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


class Shape(abc.ABC):
    pass


class Location2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Limits:
    def __init__(self, max_speed=5):
        self.max_speed = max_speed
