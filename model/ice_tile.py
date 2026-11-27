import pygame
from constants import TILE_SIZE
from model.tile import Tile


class IceTile(Tile):

    COLOR = (120, 200, 255)
    BORDER_COLOR = (100, 180, 235)
    TRACTION = 0.005
    DRIFT_SPEED = 1


    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:

        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite

        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.COLOR)

        # Reflets
        pygame.draw.line(
            surface,
            (255, 255, 255),
            (0, 6),
            (tile_size, 12),
            2
        )

        pygame.draw.line(
            surface,
            (220, 240, 255),
            (5, tile_size - 10),
            (tile_size - 5, tile_size - 4),
            1
        )

        line_color = tuple(min(255, value + 10) for value in self.COLOR)
        pygame.draw.line(
            surface, line_color, (0, 0), (tile_size - 1, 0), 1
        )
        pygame.draw.line(
            surface, line_color, (0, 0), (0, tile_size - 1), 1
        )
        self.sprite = surface
        return self.sprite