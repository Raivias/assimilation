import math
import pygame

import vector


class Bullet:
    BULLET_SIZE = 1
    BULLET_SPEED = 10

    def __init__(self, creator, team, pose, orientation, speed=BULLET_SPEED, accel=0):
        self.creator = creator
        self.team = team
        self.pose = pose
        self.speed = speed
        self.orient = orientation
        self.accel = accel

    def update(self):
        b_speed_x = math.cos(self.orient) * self.speed
        b_speed_y = math.sin(self.orient) * self.speed
        b_speed_z = 0
        b_speed = vector.Vector(b_speed_x, b_speed_y, b_speed_z)
        self.pose += b_speed

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.team,
            (int(self.pose.a), int(self.pose.b)),
            self.BULLET_SIZE
        )
