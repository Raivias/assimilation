#!/usr/bin/env python3

import math
import pygame
from pygame.locals import *
import random
import sys

import agent
import vector

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600


class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()
        self.all_agents = []
        self.screen.fill((255, 255, 255))

        for n in range(5):
            pose = vector.Vector(random.randrange(50, SCREEN_WIDTH-50), random.randrange(50, SCREEN_HEIGHT-50), 0)
            orient = math.radians(random.randrange(0, 360))
            ag = agent.Agent(pose, orient)
            self.all_agents.append(ag)

    @staticmethod
    def handle_events():
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):
        for a in self.all_agents:
            a.update()
        return

    def draw(self):
        # self.all_sprites.draw(self.screen)
        for a in self.all_agents:
            a.draw(self.screen)
        pygame.display.flip()
        pass

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ is "__main__":

    sim = Simulation()
    sim.run()
