from constants import GameState, GRID_ROWS, GRID_COLS, TILE_SIZE
from model.f1_car import FormulaCar
from model.circuit import Circuit
from model.kart_car import Kart
from model.circuits.f1_circuit import F1Circuit
from model.circuits.snow_circuit import SnowCircuit

from model.void_tile import VoidTile


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
            template = F1Circuit()

        elif circuit_id == 1:
            template = SnowCircuit()
        else:
            raise ValueError(f"Unknown circuit ID: {circuit_id}")

        self.circuit = Circuit(template.create())
        self.checkpoint_positions = getattr(template, "CHECKPOINT_POSITIONS", ())
        self.boost_positions = getattr(template, "BOOST_POSITIONS", ())
        self.visited_checkpoints: set[tuple[int, int]] = set()
        self.finish_position = getattr(template, "FINISH_POSITION", None)
        self.required_laps = getattr(template, "REQUIRED_LAPS", 3)
        self.completed_laps = 0
        self.race_finished = False
        self.was_on_finish = False
        self.spawn_car(template.START_POSITIONS[0])

    def spawn_car(self, start_position: tuple[int, int]) -> None:
        col, row = start_position
        self.car = Kart(col, row)
        self.respawn_pixel = (self.car.x, self.car.y)

    def update(self) -> None:
        """Met à jour les objets du jeu."""

        if self.state != GameState.RACING or self.circuit is None:
            return

        if self.race_finished:
            return

        # Surface sous la voiture
        current_tile = self.circuit.get_tile_at_pixel(
            self.car.x,
            self.car.y
        )

        if current_tile is not None:
            self.car.update_surface(current_tile)

        # Déplacement de la voiture
        self.car.update_position()

        # Nouvelle tuile après déplacement
        current_tile = self.circuit.get_tile_at_pixel(
            self.car.x,
            self.car.y
        )

        # Hors piste
        if current_tile is None or isinstance(current_tile, VoidTile):
            self.car.x, self.car.y = self.respawn_pixel
            self.car.vx = 0.0
            self.car.vy = 0.0
            self.car.drifting = False
            self.car.reset_steering()
            return

        # Checkpoint
        if (current_tile.col, current_tile.row) in self.checkpoint_positions:
            self.visited_checkpoints.add(
                (current_tile.col, current_tile.row)
            )

            self.respawn_pixel = (
                current_tile.col * TILE_SIZE + TILE_SIZE // 2,
                current_tile.row * TILE_SIZE + TILE_SIZE // 2
            )

        # Boost
        if (current_tile.col, current_tile.row) in self.boost_positions:
            self.car.accelerate()

        # Ligne d'arrivée
        on_finish = (
            (current_tile.col, current_tile.row)
            == self.finish_position
        )

        if on_finish and not self.was_on_finish:

            if set(self.checkpoint_positions).issubset(
                self.visited_checkpoints
            ):
                self.completed_laps += 1
                self.visited_checkpoints.clear()

                if self.completed_laps >= self.required_laps:
                    self.race_finished = True
                    self.car.vx = 0.0
                    self.car.vy = 0.0

        self.was_on_finish = on_finish