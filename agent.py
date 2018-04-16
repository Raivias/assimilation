import math
import pygame
import random
import uuid

from bullet import *
from vector import *

AGENT_SIZE = 15


class Agent():
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

    def update(self):
        self.fire()
        for b in self.bullets:
            b.update()
        return

    def fire(self):
        b_speed_x = math.cos(self.orientation) * BULLET_SPEED
        b_speed_y = math.sin(self.orientation) * BULLET_SPEED
        b_speed_z = 0
        b_speed = Vector(b_speed_x, b_speed_y, b_speed_z)
        b = Bullet(self.name, self.team, self.pose, b_speed)
        self.bullets.append(b)
        return
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.team,
            (int(self.pose.a), int(self.pose.b)),
            AGENT_SIZE
        )
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (int(self.pose.a), int(self.pose.b)),
            (int(self.pose.a + AGENT_SIZE * math.cos(self.orientation)),
             int(self.pose.b + AGENT_SIZE * math.sin(self.orientation)))
        )

        for b in self.bullets:
            b.draw(screen)
        return
    

    def in_view(self, ob):
        ob_ang = math.atan2((ob.pose.b - self.pose.b), (ob.pose.a - self.pose.a))
        # TODO finish this
