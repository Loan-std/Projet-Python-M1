import pygame
import sys
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    GameState
)
from model.game_model import GameModel
from view.game_view import GameView
from controller.input_handler import InputHandler


class GameController:
    """Controlle les inputs et le rendu."""

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.model = GameModel()
        self.view = GameView(self.screen)
        self.input_handler = InputHandler()
        self.running = True

    def run(self) -> None:
        """Commence la boucle infini du jeu."""

        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        """Gère les évènements (Appuie sur la croix pour ferméla fenêtre, appuie sur une touche,...)"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            # Lecture si une touche est pressée
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key: int) -> None:
        """Gère la ou les touches pressé en fonction de l'état de la fenêtre.

        Args:
            key (int): Nom de la touche pressée
        """

        state = self.model.state

        if state == GameState.MENU:
            self.handle_menu_key(key)
        elif state == GameState.CIRCUIT_SELECT:
            self.handle_circuit_select_key(key)

    def handle_menu_key(self, key: int) -> None:
        if key == pygame.K_RETURN:
            self.model.state = GameState.CIRCUIT_SELECT

        elif key == pygame.K_ESCAPE:
            self.quit()

    def handle_circuit_select_key(self, key: int):
        if key == pygame.K_UP:
            self.model.selected_circuit = max(
                0,
                self.model.selected_circuit - 1)

        elif key == pygame.K_DOWN:
            self.model.selected_circuit = min(
                len(self.model.available_circuits) - 1,
                self.model.selected_circuit + 1)

        elif key == pygame.K_RETURN:

            self.model.load_circuit(
                self.model.selected_circuit)
            self.model.state = GameState.RACING

        elif key == pygame.K_ESCAPE:
            self.model.state = GameState.MENU

    def update(self) -> None:
        """Mets à jour l'écran si le jeu est en pleine course."""

        if self.model.state != GameState.RACING:
            return
        
        if self.model.race_finished:
            return

        p1_input = self.input_handler.get_inputs()
        car = self.model.car
        self.apply_input(car, p1_input)
        self.model.update()

    def apply_input(self, car, player_input) -> None:
        """Applique les actions du joueur.

        Args:
            car (Class): Classe de comportement d'une voiture
            player_input (dict): Dictionnaire des inputs que doit effectuer le joueur
        """
        if player_input['accelerate']:
            car.accelerate()
        if player_input['braking']:
            car.brake()

    def render(self) -> None:
        """Dessine le rendu graphique à l'écran."""
        self.view.draw(self.model)

    def quit(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()
