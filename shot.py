import constants
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen, center=self.position, radius=self.radius, width=2, color="white")

    def update(self, dt):
        self.position += self.velocity * dt