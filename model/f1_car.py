import pygame
from model.car import Car

class FormulaCar(Car):

    ACCELERATION = 0.3
    BRAKING = 0.2
    ROTATION = 2

    def build_sprite(self):

        surf = pygame.Surface((32, 64), pygame.SRCALPHA)

        red = (220, 0, 0)
        dark_red = (150, 0, 0)
        black = (20, 20, 20)
        gray = (200, 200, 200)
        white = (240, 240, 240)

        # Aileron avant
        pygame.draw.rect(
            surf,
            gray,
            (4, 0, 24, 4),
            border_radius=1
        )

        # Nez
        pygame.draw.rect(
            surf,
            red,
            (13, 4, 6, 14),
            border_radius=3
        )

        # Roues avant
        pygame.draw.rect(
            surf,
            black,
            (0, 10, 6, 12),
            border_radius=2
        )

        pygame.draw.rect(
            surf,
            black,
            (26, 10, 6, 12),
            border_radius=2
        )

        # Châssis principal
        pygame.draw.rect(
            surf,
            red,
            (8, 16, 16, 28),
            border_radius=4
        )

        # Pontons
        pygame.draw.rect(
            surf,
            dark_red,
            (4, 20, 6, 16),
            border_radius=2
        )

        pygame.draw.rect(
            surf,
            dark_red,
            (22, 20, 6, 16),
            border_radius=2
        )

        # Cockpit
        pygame.draw.rect(
            surf,
            black,
            (11, 22, 10, 12),
            border_radius=4
        )

        # Halo
        pygame.draw.rect(
            surf,
            white,
            (12, 20, 8, 2),
            border_radius=1
        )

        # Moteur
        pygame.draw.rect(
            surf,
            dark_red,
            (10, 36, 12, 12),
            border_radius=3
        )

        # Roues arrière
        pygame.draw.rect(
            surf,
            black,
            (0, 34, 6, 16),
            border_radius=2
        )

        pygame.draw.rect(
            surf,
            black,
            (26, 34, 6, 16),
            border_radius=2
        )

        # Supports aileron arrière
        pygame.draw.rect(
            surf,
            gray,
            (10, 48, 2, 8)
        )

        pygame.draw.rect(
            surf,
            gray,
            (20, 48, 2, 8)
        )

        # Aileron arrière
        pygame.draw.rect(
            surf,
            gray,
            (2, 56, 28, 5),
            border_radius=1
        )

        return surf