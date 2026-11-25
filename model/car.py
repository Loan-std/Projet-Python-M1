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

    ACCELERATION = 0.07
    BRAKING = 0.3
    ROTATION = 3
    GRIP = 0.1
    DRIFT_DELAY = 30
    DRIFT_ON_SPEED = 7

    def __init__(self, start_col, start_row):

        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.vx = 0.0
        self.vy = 0.0
        self.angle = 0.0
        self.drifting = False
        self.left_steer_time = 0
        self.right_steer_time = 0
        self.sprite = self.build_sprite()

    def accelerate(self) -> None:
        """Augmente la vitesse x et y de la voiture en fonction de l'accélération.
        """
        radians = math.radians(self.angle)

        self.vx -= math.sin(radians) * self.ACCELERATION
        self.vy += math.cos(radians) * self.ACCELERATION

    def brake(self) -> None:
        radians = math.radians(self.angle)
        
        self.vx += math.sin(radians) * self.BRAKING
        self.vy -= math.cos(radians) * self.BRAKING

    def turn_right(self) -> None :
        """Calcul la vitesse réelle de la voiture pour pouvoir tourner lorsque la voiture est en marche.
        """
        speed = math.hypot(self.vx, self.vy)

        if speed < 1:
            self.reset_steering()
            return
            
        self.left_steer_time = 0
        self.right_steer_time += 1

        rotation = (self.ROTATION * (speed / (speed + 1)) / (1 + speed * 0.05))

        self.angle += rotation

        if (speed > self.DRIFT_ON_SPEED and self.right_steer_time >= self.DRIFT_DELAY and not self.drifting):

            self.drifting = True

            radians = math.radians(self.angle)
            side_x = math.cos(radians)
            side_y = math.sin(radians)

            drift_kick = speed * 0.2
            self.vx += side_x * drift_kick
            self.vy += side_y * drift_kick
            

    def turn_left(self) -> None:
        speed = math.hypot(self.vx, self.vy)

        if speed < 1:
            self.reset_steering()
            return

        self.left_steer_time += 1
        self.right_steer_time = 0

        rotation = (self.ROTATION * (speed / (speed + 1)) / (1 + speed * 0.05))

        self.angle -= rotation

        if (speed > self.DRIFT_ON_SPEED and self.left_steer_time >= self.DRIFT_DELAY and not self.drifting):

            self.drifting = True

            radians = math.radians(self.angle)
            side_x = math.cos(radians)
            side_y = math.sin(radians)

            drift_kick = speed * 0.2
            self.vx -= side_x * drift_kick
            self.vy -= side_y * drift_kick

    def reset_steering(self):

        self.left_steer_time = 0
        self.right_steer_time = 0

    def apply_grip(self) -> None:
        """Réduit la vitesse latérale pour limiter le dérapage."""
        grip = self.GRIP

        # pneus décrochent
        if self.drifting:
            grip *= 0.05

        radians = math.radians(self.angle)
        right_x = math.cos(radians)
        right_y = math.sin(radians)

        lateral_speed = self.vx * right_x + self.vy * right_y
        self.vx -= lateral_speed * right_x * grip
        self.vy -= lateral_speed * right_y * grip

    def update_position(self) -> None:
        """Mets à jour la position de la voiture en prenant en compte le frottement de l'air.
        """
        self.apply_grip()

        self.vx *= AIR_FRICTION
        self.vy *= AIR_FRICTION

        self.x += self.vx
        self.y += self.vy

        speed = math.hypot(self.vx, self.vy)
        if speed < 1:
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
