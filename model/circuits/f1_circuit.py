from model.circuits.circuit_template import CircuitTemplate
from model.road_tile import RoadTile
from model.grass_tile import GrassTile


class F1Circuit(CircuitTemplate):
    """
    Circuit de type Formule 1.

    Légende :
        R = Route
        G = Herbe

    Le layout est automatiquement transformé en grille grâce
    à la méthode create() héritée de CircuitTemplate.
    """

    @property
    def layout(self):
        return [
        "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
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

        return GrassTile(col, row)