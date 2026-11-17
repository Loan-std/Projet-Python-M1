import pygame
from constants import TILE_SIZE
from model.tile import Tile


class IceTile(Tile):

    COLOR = (120, 200, 255)
    BORDER_COLOR = (100, 180, 235)
    TRACTION = 0.3

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

        pygame.draw.rect(
            surface,
            self.BORDER_COLOR,
            surface.get_rect(),
            2
        )

        self.sprite = surface
        return self.sprite