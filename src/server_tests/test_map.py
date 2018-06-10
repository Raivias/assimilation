from unittest import TestCase
from unittest.mock import MagicMock
from server.map import *


class TestMap(TestCase):
    def test_none_objects(self):
        self.assertRaises(TypeError, Map(None))

    def test_objects_contains_nonMapObject(self):
        mo = MagicMock(MapObject)
        ls = [mo, "something"]
        with self.assertRaises(TypeError):
            Map(ls)

    def test_map_init_with_same_object(self):
        mo1 = MagicMock(MapObject)
        ls = [mo1, mo1]
        m = Map(ls)
        self.assertEqual(len(m.objects), 2)

    def test_map_init_with_2object(self):
        mo1 = MagicMock(MapObject)
        mo2 = MagicMock(MapObject)
        ls = [mo1, mo2]
        m = Map(ls)
        self.assertEqual(len(m.objects), 2)

    def test_map_init_with_1object(self):
        mo1 = MagicMock(MapObject)
        ls = [mo1]
        m = Map(ls)
        self.assertEqual(len(m.objects), 1)

    def test_map_init_with_0object(self):
        m = Map([])
        self.assertEqual(len(m.objects), 0)

    def test_map_add_to_empty(self):
        mo1 = MagicMock(MapObject)
        m = Map([])
        self.assertEqual(len(m.objects), 0)
        m.add_object(mo1)
        self.assertEqual(len(m.objects), 1)

    def test_map_add_first(self):
        mo1 = MagicMock(MapObject)
        mo2 = MagicMock(MapObject)
        m = Map([mo1])
        self.assertEqual(len(m.objects), 1)
        m.add_object(mo2)
        self.assertEqual(len(m.objects), 2)

    def test_map_add_second(self):
        mo1 = MagicMock(MapObject)
        mo2 = MagicMock(MapObject)
        mo3 = MagicMock(MapObject)
        m = Map([mo1])
        self.assertEqual(len(m.objects), 1)
        m.add_object(mo2)
        self.assertEqual(len(m.objects), 2)
        m.add_object(mo3)
        self.assertEqual(len(m.objects), 3)

    def test_map_add_same(self):
        mo1 = MagicMock(MapObject)
        m = Map([mo1])
        self.assertEqual(len(m.objects), 1)
        m.add_object(mo1)
        self.assertEqual(len(m.objects), 2)

    def test_move_2objects(self):
        mo1 = MagicMock(MapObject)
        mo1.move = MagicMock(return_value=mo1)
        m = Map([mo1, mo1])
        n = m.next_state()
        self.assertIsInstance(n, Map)
        self.assertEqual(len(n.objects), len(m.objects))
        self.assertEqual(mo1.move.call_count, 2)

    def test_move_1objects(self):
        mo1 = MagicMock(MapObject)
        mo1.move = MagicMock(return_value=mo1)
        m = Map([mo1])
        n = m.next_state()
        self.assertIsInstance(n, Map)
        self.assertEqual(len(n.objects), len(m.objects))
        self.assertEqual(mo1.move.call_count, 1)

    def test_move_0objects(self):
        m = Map([])
        n = m.next_state()
        self.assertIsInstance(n, Map)
        self.assertEqual(len(n.objects), len(m.objects))

    def test_different_objects_copy(self):
        # TODO this test currently fails because the mock is detected as a non-MapObject
        mo1 = MagicMock(MapObject)
        mo2 = MagicMock(MapObject)
        mo3 = MagicMock(MapObject)
        ret0 = [mo1, mo2]
        ret1 = [mo1, mo3]
        mo1.move = MagicMock(return_value=ret1)
        mo2.move = MagicMock(return_value=ret0)
        m = Map(ret0)
        m.next_state()
        mo2.move.assert_called_once_with(ret0)


class TestMapObject(TestCase):
    def test_init_no_problems(self):
        loc = MagicMock(Location2D)
        s = MagicMock(Shape)
        lim = MagicMock(Limits)
        with self.assertRaisesRegex(TypeError, "Can't instantiate abstract class MapObject with abstract methods move"):
            MapObject(loc, s, lim)