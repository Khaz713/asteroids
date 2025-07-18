import constants
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, center=self.position, radius=self.radius, width=2, color="white")

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2