import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

clock = pygame.time.Clock()
dt = 0.0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
print(updatable)
print(drawable)
Player.containers = (updatable, drawable)

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        print(f"updatable: {updatable.spritedict}")
        print(f"drawable: {drawable.spritedict}")
        log_state()
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            for sprite in drawable:
                sprite.draw(screen)
            updatable.update(dt)
            pygame.display.flip()





if __name__ == "__main__":
    main()
