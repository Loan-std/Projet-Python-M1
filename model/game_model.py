from constants import GameState, GRID_ROWS, GRID_COLS
from model.f1_car import FormulaCar
from model.circuit import Circuit

from model.circuits.f1_circuit import F1Circuit
from model.circuits.snow_circuit import SnowCircuit


class GameModel:
    """Gère le rendu du jeu à l'écran.
    """

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: FormulaCar | None = None
        self.selected_circuit = 0
        self.available_circuits = ["Formule 1", "Hivernale"]

    def load_circuit(self, circuit_id: int) -> None:

        if circuit_id == 0:
            grid = F1Circuit().create()
            self.circuit = Circuit(grid)
            self.spawn_car(7, 1)

        elif circuit_id == 1:
            grid = SnowCircuit().create()
            self.circuit = Circuit(grid)
            self.spawn_car(7, 1)

    def spawn_car(self, x, y) -> None:
        self.car = FormulaCar(x, y)

    def update(self) -> None:
        """Mets à jour les objets dans l'écran.
        """
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
