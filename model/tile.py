import pygame
from abc import ABC
from constants import TILE_SIZE


class Tile(ABC):
    """
    Classe de base pour toutes les tuiles.

    Une tuile possède :
    - une position dans la grille
    - un sprite mis en cache
    - une couleur spécifique définie par les classes filles
    """

    COLOR = (0, 0, 0)
    TRACTION = 1.0

    def __init__(self, col: int, row: int):
        self.col = col
        self.row = row
        self.sprite: pygame.Surface | None = None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:

        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite

        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.COLOR)

        pygame.draw.rect(
            surface,
            self.BORDER_COLOR,
            surface.get_rect(),
            2
        )

        self.sprite = surface
        return self.sprite