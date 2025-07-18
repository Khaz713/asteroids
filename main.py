import pygame
import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    clock = pygame.time.Clock()
    dt = 0  # delta time

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    asteroids_field = AsteroidField()
    font = pygame.font.SysFont("Helvetica Bold", 50)

    score = 0
    lives = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                lives -= 1
                if lives == 0:
                    print(f"GAME OVER\n"
                          f"FINAL SCORE: {score}")
                    return
                player.kill()
                player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
                for asteroid_wipe in asteroids:
                    asteroid_wipe.kill()


            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    score += 1

        screen.fill("black")
        screen.blit(font.render(f"SCORE: {score}", True, "black", "white"), (0, 0))
        screen.blit(font.render(f"LIVES: {lives}", True, "black", "white"), (0, 34))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
