import constants
import circleshape
import pygame
from shot import Shot


class Player(circleshape.CircleShape):

    def __init__(self, x, y):
        circleshape.CircleShape.__init__(self, x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.speed = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
        self.timer = constants.PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # forward
            self.speed += constants.PLAYER_ACCELERATION
            if self.speed > constants.PLAYER_MAX_SPEED:
                self.speed = constants.PLAYER_MAX_SPEED
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:  # back
            self.speed -= constants.PLAYER_ACCELERATION
            if self.speed < -constants.PLAYER_MAX_SPEED:
                self.speed = -constants.PLAYER_MAX_SPEED
        else:
            if self.speed < 0:
                self.speed += constants.PLAYER_DECELERATION
                if self.speed > 0:
                    self.speed = 0
            if self.speed > 0:
                self.speed -= constants.PLAYER_DECELERATION
                if self.speed < 0:
                    self.speed = 0
        self.move(dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # left
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # right
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if not self.timer > 0:
                self.shoot()
