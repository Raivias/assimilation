from mapobject import *


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
