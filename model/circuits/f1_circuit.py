from model.circuits.circuit_template import CircuitTemplate
from model.road_tile import RoadTile
from model.grass_tile import GrassTile
from model.dirt_tile import DirtTile
from model.void_tile import VoidTile
from model.ice_tile import IceTile


class F1Circuit(CircuitTemplate):
    """
    Circuit de type Formule 1.

    Légende :
        R = Route
        G = Herbe
        D = Terre
        V = Vide

    Le layout est automatiquement transformé en grille grâce
    à la méthode create() héritée de CircuitTemplate.
    """

    START_POSITIONS = ((7, 2), (7, 4))
    START_ANGLE = 90.0
    CHECKPOINT_POSITIONS = ((7, 20),)
    CHECKPOINT_ANGLES = {(7, 20): -90.0}
    FINISH_POSITION = (7, 2)
    REQUIRED_LAPS = 3
    BOOST_POSITIONS = ((15, 2),)

    @property
    def layout(self):
        return [
            "GDVGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
            "GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRG",
            "GRRRRRGGGGGGGGGGGGGGGGGGGGRRRRRG",
            "GRRRRRGGGGGGGGGGGGGGGGGGGGRRRRRG",
            "GRRRRRGGGGGGGGGGGGGGGGGGGGRRRRRG",
            "GRRRRRGGGGRRRRRRRRRRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRRRRRRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRRRRRRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRRRRRRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRRRRRRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRGGGGRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRGGGGRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRGGGGRRRRRGGRRRRRG",
            "GRRRRRGGGGRRRRRGGGGRRRRRGGRRRRRG",
            "GRRRRRRRRRRRRRRGGGGRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRGGGGRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRGGGGRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRGGGGRRRRRRRRRRRRG",
            "GRRRRRRRRRRRRRRGGGGRRRRRRRRRRRRG",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        ]

    def get_tile(self, character, col, row):

        if character == "R":
            if 1 <= row <= 5 and 10 <= col <= 23:
                return DirtTile(col, row)

            if 8 <= row <= 15 and 26 <= col <= 30:
                return IceTile(col, row)

            return RoadTile(col, row)

        if character == "I":
            return IceTile(col, row)

        if character == "D":
            return DirtTile(col, row)

        if character == "V":
            return VoidTile(col, row)

        return GrassTile(col, row)