import pygame
import sys

from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Setting up the clock
    clock = pygame.time.Clock()
    dt = 0.0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	#Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    a_field = AsteroidField()

    # Shots
    Shot.containers = (shots, drawable, updatable)

    # Initializing pygame and displaying info on start
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game Loop
    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)

        # Check collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Display screen
        pygame.display.flip()

        log_state()





if __name__ == "__main__":
    main()
