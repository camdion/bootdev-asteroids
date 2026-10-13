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

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_vel1 = self.velocity.rotate(split_angle)
        split_vel2 = self.velocity.rotate(-split_angle)
        # smaller_radius
