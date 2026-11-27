from model.circuits.circuit_template import CircuitTemplate
from model.road_tile import RoadTile
from model.snow_tile import SnowTile
from model.ice_tile import IceTile
from model.grass_tile import GrassTile
from model.void_tile import VoidTile

class SnowCircuit(CircuitTemplate):
    """
    Circuit de type Hivernale.

    Légende :
        R = Route
        N = Neige
        I = Glace

    Le layout est automatiquement transformé en grille grâce
    à la méthode create() héritée de CircuitTemplate.
    """

    START_POSITIONS = ((7, 1), (8, 1))
    CHECKPOINT_POSITIONS = ((12, 16),)
    FINISH_POSITION = (7, 1)
    REQUIRED_LAPS = 3
    BOOST_POSITIONS = ((15, 1),)

    @property
    def layout(self):
        return [
            "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
            "NRRRRRRRRRRRIIIIIIIIIIIIRRRRRRRN",
            "NRRRRRRRRRRRIIIIIIIIIIIIRRRRRRRN",
            "NRRRRRRRRRRRIIIIIIIIIIIIRRRRRRRN",
            "NRRRRRRRRRRRIIIIIIIIIIIIRRRRRRRN",
            "NRRRRRRRRRRRIIIIIIIIIIIIRRRRRRRN",
            "NRRRRRNNNNNNNNNNNNNNNNNNNNRRRRRN",
            "NRRRRRNNNNNNNNNNNNNNNNNNNNIIIIIN",
            "NRRRRRNNNNNNNNNNNNNNNNNNNNIIIIIN",
            "NRRRRRRRRRRRRRRNNNNNNNNNNNIIIIIN",
            "NRRRRRRRRRRRRRRNNNNNNNNNNNIIIIIN",
            "NRRRRRRRRRRRRRRNNNNNNNNNNNIIIIIN",
            "NRRRRRRRRRRRRRRNNNNNNNNNNNIIIIIN",
            "NRRRRRRRRRRRRRRNNNNNNNNNNNIIIIIN",
            "NNNNNNNNNNRRRRRNNNNNNNNNNNIIIIIN",
            "NNNNNNNNNNRRRRRNNNNNNNNNNNIIIIIN",
            "NNNNNNNNNNRRRRRNNNNNNNNNNNRRRRRN",
            "NNNNNNNNNNRRRRRNNNNNNNNNNNRRRRRN",
            "NNNNNNNNNNRRRRRRRRRRRRRRRRRRRRRN",
            "NNNNNNNNNNRRRRRRRRRRRRRRRRRRRRRN",
            "NNNNNNNNNNRRRRRRRRRRRRRRRRRRRRRN",
            "NNNNNNNNNNRRRRRRRRRRRRRRRRRRRRRN",
            "NNNNNNNNNNRRRRRRRRRRRRRRRRRRRRRN",
            "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        ]

    def get_tile(self, character, col, row):

        if character == "R":
            if 18 <= row <= 22 and 16 <= col <= 25:
                return GrassTile(col, row)

            return RoadTile(col, row)
        
        if character == "N":
            if 17 <= row <= 22 and 1 <= col <= 6:
                return VoidTile(col, row)

            if 9 <= row <= 14 and 18 <= col <= 22:
                return VoidTile(col, row)

            return SnowTile(col, row)
        
        if character == "I":
            return IceTile(col, row)