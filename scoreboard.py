import pygame

from constants import *

class Scoreboard(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.current_score = 0

    def add_points(self, points: int) -> None:
        if points <= 0:
            return
        self.current_score += points


    def draw(self, screen: pygame.Surface) -> None:
        display_text = pygame.font.Font(pygame.font.get_default_font(), 12)
        display_text_surface = display_text.render(f"Current Score: {self.current_score}", False, "white")
        screen.blit(display_text_surface, (SCREEN_WIDTH / 2, 12))
