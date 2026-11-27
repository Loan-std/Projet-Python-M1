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
        self.car_p1: FormulaCar | None = None
        self.car_p2: Kart | None = None
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
        self.checkpoint_angles = getattr(template, "CHECKPOINT_ANGLES", {})
        self.boost_positions = getattr(template, "BOOST_POSITIONS", ())
        self.checkpoint_lines = template.CHECKPOINT_LINES
        self.checkpoint_line_angles = template.CHECKPOINT_LINE_ANGLES
        self.visited_checkpoints: set[int] = set()
        self.finish_position = getattr(template, "FINISH_POSITION", None)
        self.finish_line = template.FINISH_LINE
        self.required_laps = getattr(template, "REQUIRED_LAPS", 3)
        self.completed_laps = 0
        self.race_finished = False
        self.was_on_finish = False
        self.start_angle = getattr(template, "START_ANGLE", 0.0)
        self.spawn_car(template.START_POSITIONS[0], template.START_POSITIONS[1])

    def spawn_car(self, start_position_p1: tuple[int, int], start_position_p2: tuple[int, int]) -> None:
        col_p1, row_p1 = start_position_p1
        col_p2, row_p2 = start_position_p2
        self.car_p1 = FormulaCar(col_p1, row_p1)
        self.car_p2 = Kart(col_p2, row_p2)
        self.car_p1.angle = self.start_angle
        self.car_p2.angle = self.start_angle

        self.respawn_p1 = (
            self.car_p1.x,
            self.car_p1.y,
            self.start_angle
        )

        self.respawn_p2 = (
            self.car_p2.x,
            self.car_p2.y,
            self.start_angle
        )

    def update(self) -> None:
        """Met à jour les objets du jeu."""

        if self.state != GameState.RACING or self.circuit is None:
            return

        if self.race_finished:
            return

        for car, respawn_attr in ((self.car_p1, "respawn_p1"), (self.car_p2, "respawn_p2")):

            if car is None:
                continue

            # Surface actuelle
            current_tile = self.circuit.get_tile_at_pixel(
                car.x,
                car.y
            )

            if current_tile is not None:
                car.update_surface(current_tile)

            # Déplacement
            car.update_position()

            # Nouvelle tuile après déplacement
            current_tile = self.circuit.get_tile_at_pixel(
                car.x,
                car.y
            )

            # Hors piste
            if current_tile is None or isinstance(current_tile, VoidTile):
                respawn_x, respawn_y, respawn_angle = getattr(self, respawn_attr)
                
                car.x = respawn_x
                car.y = respawn_y
                car.angle = respawn_angle
                car.vx = 0.0
                car.vy = 0.0
                car.drifting = False
                car.reset_steering()

                continue

            # Checkpoint
            position = (current_tile.col, current_tile.row)

            for checkpoint_id, line in enumerate(self.checkpoint_lines):
                if position in line:
                    self.visited_checkpoints.add(checkpoint_id)
                    col, row = line[len(line) // 2]
                    setattr(self, respawn_attr,(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2, self.checkpoint_line_angles[checkpoint_id]))

            # Boost
            if (current_tile.col, current_tile.row) in self.boost_positions:
                car.accelerate()

        # Gestion arrivée (joueur 1 uniquement pour l'instant)
        if self.car_p1 is None:
            return

        current_tile = self.circuit.get_tile_at_pixel(
            self.car_p1.x,
            self.car_p1.y
        )

        if current_tile is None:
            return

        on_finish = (
            (current_tile.col, current_tile.row) in self.finish_line
        )

        if on_finish and not self.was_on_finish:

            if len(self.visited_checkpoints) == len(self.checkpoint_lines):
                self.completed_laps += 1
                self.visited_checkpoints.clear()

                if self.completed_laps >= self.required_laps:
                    self.race_finished = True

                    self.car_p1.vx = 0.0
                    self.car_p1.vy = 0.0

                    if self.car_p2:
                        self.car_p2.vx = 0.0
                        self.car_p2.vy = 0.0

        self.was_on_finish = on_finish