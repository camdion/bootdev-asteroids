from pygame.key import ScancodeWrapper
from shot import Shot
import pygame

from circleshape import CircleShape
from constants import *

Surface = pygame.Surface

class Player(CircleShape):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PLAYER_RADIUS)
        self.__rotation = 0
        self.__timer = 0.0
        self.__velocity = float(PLAYER_SPEED)

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.__rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
            self.__velocity *= PLAYER_ACCELERATION
        if keys[pygame.K_s]:
            self.move(-dt)
            self.__velocity *= PLAYER_ACCELERATION
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.__timer -= dt

    def move(self, dt: float) -> None:
        dir = pygame.Vector2(0, 1).rotate(self.__rotation)
        self.position += dir * self.__velocity * dt

    def shoot(self) -> None:
        if self.__timer > 0:
            return
        else:
            self.__timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.__rotation) * PLAYER_SHOOT_SPEED

    def reset_speed(self) -> None:
        self.__velocity = PLAYER_SPEED
