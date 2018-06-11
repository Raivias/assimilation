from server.map import *


class TestAgent(MapObject):
    def move(self, current_state):
        pass


class TestAgentShape(Shape):
    radius = 5


class TestLimits(Limits):
    def __init__(self):
        super(TestLimits, self).__init__()
