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
        obs = []
        for ob in self.objects:
            obs.append(ob.move())
        new_map = Map(obs)
        return new_map


class MapObject(abc.ABC):
    def __init__(self, location, shape, limits):
        if not isinstance(location, Location):
            raise TypeError("location was not of type Location")
        self.location = location

        if not isinstance(shape, Shape):
            raise TypeError("shape was not of type Shape")
        self.shape = shape

        if not isinstance(limits, Limits):
            raise TypeError("limits was not of type Limits")
        self.limits = limits

    @abc.abstractmethod
    def move(self):
        return MapObject(self.location, self.shape, self.limits)


class Shape:
    # TODO
    def __init__(self):
        pass


class Location:
    # TODO
    def __init__(self):
        pass


class Limits:
    # TODO
    def __init__(self):
        pass
