import math
import pygame
import random
import uuid

from vector import *

AGENT_SIZE = 15


class Agent(pygame.sprite.Sprite):
    def __init__(self, groups, pose, orientation=0, team=None):
        super().__init__(groups)
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

        """Set up shape"""
        self.image = pygame.Surface((AGENT_SIZE, AGENT_SIZE))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.x = pose.a
        self.rect.y = pose.b
        self.rect.center = (900 / 2, 600 / 2)

    def update(self):
        self.rect.x += 5
        return

    def draw(self, surface):
        pygame.draw.circle(
            self.image,
            self.team,
            (int(self.pose.a), int(self.pose.b)),
            AGENT_SIZE
        )
        pygame.draw.line(
            self.image,
            (0, 0, 0),
            (int(self.rect.center[0]), int(self.rect.center[1])),
            (int(self.rect.center[0] + AGENT_SIZE * math.cos(self.orientation)),
             int(self.rect.center[1] + AGENT_SIZE * math.sin(self.orientation)))
        )

    """
    def fire(self):
        b_speed_x = math.cos(self.orientation) * BULLET_SPEED
        b_speed_y = math.sin(self.orientation) * BULLET_SPEED
        b_speed_z = 0
        b_speed = Vector(b_speed_x, b_speed_y, b_speed_z)
        b = Bullet(self.groups(), self.name, self.team, self.pose, b_speed)
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
    """