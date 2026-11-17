import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_BRAKING, CAR_ROTATION, FROTTEMENT_AIR, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)


class Car:
    """Décrit le comportement d'une voiture. Pour pouvoir gérer le dérapage, on sépare la vitesse sur x et y.
    """

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.vx: float = 0.0        # vitesse sur X
        self.vy: float = 0.0        # vitesse sur Y
        self.angle: float = 0.0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Augmente la vitesse x et y de la voiture en fonction de l'accélération.
        """
        radians = math.radians(self.angle)

        self.vx += math.sin(radians) * CAR_ACCELERATION
        self.vy -= math.cos(radians) * CAR_ACCELERATION

    def brake(self) -> None:
        radians = math.radians(self.angle)
        
        self.vx -= math.sin(radians) * CAR_BRAKING
        self.vy += math.cos(radians) * CAR_BRAKING

    def turn_right(self) -> None :
        """Calcul la vitesse réelle de la voiture pour pouvoir tourner lorsque la voiture est en marche.
        """
        speed = math.hypot(self.vx, self.vy)

        if speed > 0.2:
            self.angle += CAR_ROTATION

    def turn_left(self) -> None :
        speed = math.hypot(self.vx, self.vy)

        if speed > 0.2:
            self.angle -= CAR_ROTATION

    def update_position(self) -> None:
        """Mets à jour la position de la voiture en prenant en compte le frottement de l'air.
        """

        self.vx *= FROTTEMENT_AIR
        self.vy *= FROTTEMENT_AIR

        self.x += self.vx
        self.y += self.vy

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
