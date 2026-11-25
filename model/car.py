import pygame
import math
from constants import (
    AIR_FRICTION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE
)

from abc import ABC
import pygame
import math

class Car(ABC):
    """Décrit le comportement d'une voiture. Pour pouvoir gérer le dérapage, on sépare la vitesse sur x et y.
    """

    ACCELERATION = 0.2
    BRAKING = 0.1
    ROTATION = 3
    DRIFT_DELAY = 30

    def __init__(self, start_col, start_row):

        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.vx = 0.0
        self.vy = 0.0
        self.angle = 0.0
        self.drifting = False
        self.left_steer_time = 0
        self.right_steer_time = 0
        self.current_grip = 1
        self.current_drift_speed = 10
        self.current_steering = 1
        self.current_speed_multiplier = 1
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Augmente la vitesse x et y de la voiture en fonction de l'accélération.
        """
        radians = math.radians(self.angle)

        self.vx += math.sin(radians) * self.ACCELERATION
        self.vy -= math.cos(radians) * self.ACCELERATION

    def brake(self) -> None:
        radians = math.radians(self.angle)
        braking = self.BRAKING * max(0.3, self.current_grip)

        self.vx -= math.sin(radians) * braking
        self.vy += math.cos(radians) * braking

    def turn_right(self) -> None :
        """Calcul la vitesse réelle de la voiture pour pouvoir tourner lorsque la voiture est en marche.
        """
        speed = math.hypot(self.vx, self.vy)

        if speed < 1:
            self.reset_steering()
            return
            
        self.left_steer_time = 0
        self.right_steer_time += 1

        rotation = (
            self.ROTATION
            * self.current_steering
            * (speed / (speed + 1))
            / (1 + speed * 0.05)
        )

        self.angle += rotation

        if (speed > self.current_drift_speed and self.right_steer_time >= self.DRIFT_DELAY and not self.drifting):
            self.drifting = True
            

    def turn_left(self) -> None:
        speed = math.hypot(self.vx, self.vy)

        if speed < 1:
            self.reset_steering()
            return

        self.left_steer_time += 1
        self.right_steer_time = 0

        rotation = (
            self.ROTATION
            * self.current_steering
            * (speed / (speed + 1))
            / (1 + speed * 0.05)
        )
        self.angle -= rotation

        if (speed > self.current_drift_speed and self.left_steer_time >= self.DRIFT_DELAY and not self.drifting):
            self.drifting = True

    def update_surface(self, tile):

        self.current_grip = tile.TRACTION
        self.current_drift_speed = tile.DRIFT_SPEED
        self.current_speed_multiplier = tile.SPEED_MULTIPLIER
        self.current_steering = tile.STEERING

    def reset_steering(self):

        self.left_steer_time = 0
        self.right_steer_time = 0

    def apply_grip(self) -> None:

        radians = math.radians(self.angle)

        forward_x = -math.sin(radians)
        forward_y = math.cos(radians)

        right_x = math.cos(radians)
        right_y = math.sin(radians)

        # vitesse dans l'axe de la voiture
        forward_speed = (
            self.vx * forward_x +
            self.vy * forward_y
        )

        # vitesse latérale
        lateral_speed = (
            self.vx * right_x +
            self.vy * right_y
        )

        grip = self.current_grip

        if self.drifting:
            grip *= 0.1

        lateral_speed *= (1 - grip)

        self.vx = (
            forward_x * forward_speed +
            right_x * lateral_speed
        )

        self.vy = (
            forward_y * forward_speed +
            right_y * lateral_speed
        )

    def update_position(self) -> None:
        """Mets à jour la position de la voiture en prenant en compte le frottement de l'air.
        """
        self.apply_grip()

        self.vx *= AIR_FRICTION * self.current_speed_multiplier
        self.vy *= AIR_FRICTION * self.current_speed_multiplier

        self.x += self.vx
        self.y += self.vy

        speed = math.hypot(self.vx, self.vy)

        if speed < self.current_drift_speed * 0.5:
            self.drifting = False
            self.reset_steering()

    def build_sprite(self) -> pygame.Surface:
        surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surf, (255, 0, 0), (0, 0, CAR_WIDTH,
                         CAR_HEIGHT), border_radius=5)
        return surf

    def get_rotated_sprite(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Change l'orientation de la voiture.
        """

        rotated = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        return rotated, rect
