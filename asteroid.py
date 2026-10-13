#Asteroid
import random
import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event

Surface = pygame.Surface

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> int:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 10

        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_vel1 = self.velocity.rotate(split_angle)
        split_vel2 = self.velocity.rotate(-split_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        ast1.velocity = split_vel1 * 1.2

        ast2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        ast2.velocity = split_vel2 * 1.2

        return int(self.radius // ASTEROID_MIN_RADIUS) * 10
