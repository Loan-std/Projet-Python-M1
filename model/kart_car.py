import pygame
from model.car import Car


class Kart(Car):

    ACCELERATION = 0.35
    BRAKING = 0.15
    ROTATION = 3.5

    def build_sprite(self):

        surf = pygame.Surface((32, 48), pygame.SRCALPHA)

        red = (220, 40, 40)
        dark_red = (160, 20, 20)
        black = (25, 25, 25)
        gray = (120, 120, 120)
        blue = (40, 120, 255)
        yellow = (255, 220, 0)

        # Roues avant
        pygame.draw.rect(
            surf,
            black,
            (1, 6, 6, 10),
            border_radius=2
        )

        pygame.draw.rect(
            surf,
            black,
            (25, 6, 6, 10),
            border_radius=2
        )

        # Roues arrière
        pygame.draw.rect(
            surf,
            black,
            (1, 28, 6, 12),
            border_radius=2
        )

        pygame.draw.rect(
            surf,
            black,
            (25, 28, 6, 12),
            border_radius=2
        )

        # Pare-choc avant
        pygame.draw.rect(
            surf,
            gray,
            (7, 2, 18, 5),
            border_radius=2
        )

        # Châssis
        pygame.draw.rect(
            surf,
            red,
            (7, 6, 18, 32),
            border_radius=5
        )

        # Siège
        pygame.draw.rect(
            surf,
            dark_red,
            (10, 20, 12, 10),
            border_radius=3
        )

        # Pilote
        pygame.draw.circle(
            surf,
            yellow,
            (16, 16),
            6
        )

        # Casque
        pygame.draw.circle(
            surf,
            blue,
            (16, 16),
            5
        )

        # Visière
        pygame.draw.rect(
            surf,
            (30, 30, 30),
            (13, 14, 6, 3),
            border_radius=1
        )

        # Volant
        pygame.draw.circle(
            surf,
            black,
            (16, 24),
            3,
            1
        )

        # Colonne de direction
        pygame.draw.line(
            surf,
            black,
            (16, 19),
            (16, 22),
            2
        )

        # Moteur arrière
        pygame.draw.rect(
            surf,
            gray,
            (10, 36, 12, 6),
            border_radius=2
        )

        # Échappement gauche
        pygame.draw.rect(
            surf,
            black,
            (11, 42, 3, 4),
            border_radius=1
        )

        # Échappement droit
        pygame.draw.rect(
            surf,
            black,
            (18, 42, 3, 4),
            border_radius=1
        )

        # Petit spoiler arrière
        pygame.draw.rect(
            surf,
            dark_red,
            (7, 44, 18, 3),
            border_radius=1
        )

        return surf