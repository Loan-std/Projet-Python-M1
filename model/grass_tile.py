from model.tile import Tile


class GrassTile(Tile):

    COLOR = (50, 160, 50)
    BORDER_COLOR = (30, 120, 30)
    TRACTION = 0.3
    DRIFT_SPEED = 5
    SPEED_MULTIPLIER = 0.9
    STEERING = 0.8