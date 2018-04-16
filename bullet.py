import pygame

BULLET_SIZE = 1
BULLET_SPEED = 10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, creator, team, pose, speed=(0, 0, 0), accel=(0, 0, 0)):
        super().__init__(groups)
        self.creator = creator
        self.team = team
        self.pose = pose
        self.speed = speed
        self.accel = accel

    def step(self):
        self.pose = self.pose + self.speed

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.team,
            (int(self.pose.a), int(self.pose.b)),
            BULLET_SIZE
        )
