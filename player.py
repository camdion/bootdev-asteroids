import pygame

from circleshape import CircleShape
from constants import *

Surface = pygame.Surface

class Player(CircleShape):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PLAYER_RADIUS)
        self.__rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
