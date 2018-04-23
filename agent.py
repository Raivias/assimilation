import random
import uuid

from bullet import *
from vector import *


class Agent:
    AGENT_RADIUS = 7
    AGENT_SPEED = 1

    def __init__(self, pose, orientation=0, team=None):
        if team is None:
            team = (
                random.randrange(80, 250),
                random.randrange(80, 250),
                random.randrange(80, 250)
            )
        """Set fields"""
        self.name = uuid.uuid4()
        self.team = team
        self.pose = pose
        self.orientation = orientation
        self.speed = Vector(0, 0, 0)
        self.accel = Vector(0, 0, 0)
        self.bullets = []

    def update(self, items):
        self.check_hit(items)
        for b in self.bullets:
            b.update()
        return
    
    def draw(self, screen):
        self.keep_onscreen(screen, self)
        pygame.draw.circle(
            screen,
            self.team,
            (int(self.pose.a), int(self.pose.b)),
            self.AGENT_RADIUS
        )
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (int(self.pose.a), int(self.pose.b)),
            (int(self.pose.a + self.AGENT_RADIUS * math.cos(self.orientation)),
             int(self.pose.b + self.AGENT_RADIUS * math.sin(self.orientation)))
        )

        for b in self.bullets:
            self.keep_onscreen(screen, b)
            b.draw(screen)
        return

    def check_hit(self, agents):
        for a in agents:
            for b in a.bullets:
                dis, angle = self.distance_and_angle_to_object(b)
                if dis <= self.AGENT_RADIUS:
                    self.team = b.team
                    a.bullets.remove(b)
                    return True
        return False

    @staticmethod
    def keep_onscreen(screen, object):
        width, height = screen.get_size()
        object.pose.a = object.pose.a % width
        object.pose.b = object.pose.b % height
        return

    def distance_and_angle_to_object(self, object):
        p = self.pose - object.pose
        distance = math.sqrt(math.pow(p.a, 2) + math.pow(p.b, 2))
        angle = math.atan2(p.b, p.a)
        return distance, angle

    def fire(self):
        self.bullets.append(Bullet(self, self.team, self.pose, self.orientation))
        return
