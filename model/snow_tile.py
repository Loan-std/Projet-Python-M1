from model.tile import Tile


class SnowTile(Tile):

    COLOR = (240, 240, 240)
    BORDER_COLOR = (210, 210, 210)
    TRACTION = 0.3
    DRIFT_SPEED = 5
    SPEED_MULTIPLIER = 0.93
    STEERING = 0.8