from model.circuits.circuit_template import CircuitTemplate
from model.road_tile import RoadTile
from model.grass_tile import GrassTile
from model.dirt_tile import DirtTile
from model.void_tile import VoidTile


class F1Circuit(CircuitTemplate):
    """
    Circuit de type Formule 1.

    Légende :
        R = Route
        G = Herbe

    Le layout est automatiquement transformé en grille grâce
    à la méthode create() héritée de CircuitTemplate.
    """

    START_POSITIONS = ((7, 1), (8, 1))
    CHECKPOINT_POSITIONS = ((7, 20),)
    @property
    def layout(self):
        return [
        "GDVGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        "GGGGRRRRRRRRRRRRRRRRRRRRRRRRGGGG",
        "GGGRRRRRRRRRRRRRRRRRRRRRRRRRRGGG",
        "GGGRRRRRRRRRRRRRRRRRRRRRRRRRRGGG",
        "GGGRRRRGGGGGGGGGGGGGGGGGGRRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRGGGGGGGGGGGGGGGGGGGGRRRGGG",
        "GGGRRRRGGGGGGGGGGGGGGGGGGRRRRGGG",
        "GGGRRRRRRRRRRRRRRRRRRRRRRRRRRGGG",
        "GGGRRRRRRRRRRRRRRRRRRRRRRRRRRGGG",
        "GGGGRRRRRRRRRRRRRRRRRRRRRRRGGGGG",
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    ]

    def get_tile(self, character, col, row):

        if character == "R":
            return RoadTile(col, row)

        if character == "D":
            return DirtTile(col, row)

        if character == "V":
            return VoidTile(col, row)

        return GrassTile(col, row)