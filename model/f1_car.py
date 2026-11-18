import pygame
from model.car import Car

class FormulaCar(Car):

    ACCELERATION = 0.35
    BRAKING = 0.1
    ROTATION = 2

    def build_sprite(self):

        surf = pygame.Surface((20, 40), pygame.SRCALPHA)

        pygame.draw.rect(
            surf,
            (220, 0, 0),
            (0, 0, 20, 40),
            border_radius=3
        )

        return surf