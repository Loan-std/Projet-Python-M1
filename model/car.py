import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_BRAKING, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:
    """Décrit le comportement d'une voiture."""

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Augmente la vitesse de la voiture en fonction de l'accélération."""

        self.speed += CAR_ACCELERATION

    def brake(self) -> None:
        self.speed -= CAR_BRAKING

    def update_position(self) -> None:
        """Mets à jour la position de la voiture."""

        self.y += self.speed

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Change l'orientation de la voiture."""

        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
