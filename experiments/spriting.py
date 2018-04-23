import pygame
from pygame.locals import *
import random
import sys

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600


class Item(pygame.sprite.Sprite):
    ITEM_SIZE = 15
    ITEM_SPEED = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((self.ITEM_SIZE, self.ITEM_SIZE))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT))
        circle = pygame.draw.circle(self.image, (250, 0, 0,), self.rect.center, 10)
        self.image.fill((0, 255, 255), circle)
        return

    def draw(self):
        pygame.draw.circle(self.image, (250, 0, 0,), self.rect.center, self.ITEM_SIZE)
        return

    def update(self):
        if self.rect.x != SCREEN_WIDTH / 2:
            self.rect.x += self.ITEM_SPEED * -1 if self.rect.x >= (SCREEN_WIDTH / 2) else self.ITEM_SPEED

        if self.rect.y != SCREEN_HEIGHT / 2:
            self.rect.y += self.ITEM_SPEED * -1 if self.rect.y >= (SCREEN_HEIGHT / 2) else self.ITEM_SPEED
        return


class Sim:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption("Experiment")
        self.clock = pygame.time.Clock()
        self.items = pygame.sprite.Group()
        self.screen.fill((255, 255, 255))

        for _ in range(2):
            i = Item()
            self.items.add(i)

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

    def run(self):
        while True:
            self.handle_events()
            self.items.update()
            self.screen.fill((255, 255, 255))
            self.items.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    sim = Sim()
    sim.run()