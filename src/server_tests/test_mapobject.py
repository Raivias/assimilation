from unittest import TestCase
from unittest.mock import MagicMock
from server.mapobject import *


class TestMapObject(TestCase):
    def test_init_no_problems(self):
        loc = MagicMock(Location2D)
        s = MagicMock(Shape)
        lim = MagicMock(Limits)
        with self.assertRaisesRegex(TypeError, "Can't instantiate abstract class MapObject with abstract methods move"):
            MapObject(loc, s, lim)
