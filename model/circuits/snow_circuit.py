from model.circuits.circuit_template import CircuitTemplate
from model.road_tile import RoadTile
from model.snow_tile import SnowTile
from model.ice_tile import IceTile

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
    CHECKPOINT_POSITIONS = ((7, 18),)
    FINISH_POSITION = (7, 1)
    REQUIRED_LAPS = 3
    BOOST_POSITIONS = ((15, 1),)

    @property
    def layout(self):
        return [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "NNNNNNRRRRRRRRRRRRRRRRRNNNNNNNNN",
        "NNNNNRRIIIIIIIIIIIIIIIRRNNNNNNNN",
        "NNNNRRIINNNNNNNNNNNNNNIIRRNNNNNN",
        "NNNRRIINNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIINNNNNNNNNNNNNNNNNIIRRNNNNN",
        "NNRRIINNNNNNNNNNNNNNNNNIIRRNNNNN",
        "NNRRIINNNNNIIIIIIINNNNNIIRRNNNNN",
        "NNRRIINNNNIIIIIIIINNNNNIIRRNNNNN",
        "NNRRIINNNNIIIIIIIINNNNNIIRRNNNNN",
        "NNRRIINNNNIIIIIIINNNNNIIRRNNNNNN",
        "NNRRIINNNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIINNNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIINNNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIIINNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIIINNNNNNNNNNNNNNNIIRRNNNNNN",
        "NNRRIINNNNNNNNNNNNNNNIIIRRNNNNNN",
        "NNNRRIIIIIIIIIIIIIIIIIIRRNNNNNNN",
        "NNNNRRRRRRRRRRRRRRRRRRRRNNNNNNNN",
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
    ]

    def get_tile(self, character, col, row):

        if character == "R":
            return RoadTile(col, row)
        if character == "N":
            return SnowTile(col, row)
        if character == "I":
            return IceTile(col, row)