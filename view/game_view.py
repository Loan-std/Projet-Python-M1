import pygame
from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COLOR_PANEL, COLOR_PANEL_BORDER,
    GameState
)
from model.game_model import GameModel


class GameView:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, model: GameModel) -> None:
        """Dessine sur l'écran en fonction de l'état du jeu.

        Args:
            model (GameModel): classe du dossier 'model'
        """
        self.screen.fill(COLOR_BG)
        if model.state == GameState.MENU:
            self._draw_menu(model)
        elif model.state == GameState.RACING:
            self._draw_racing(model)
        elif model.state == GameState.CIRCUIT_SELECT:
            self._draw_circuit_select(model)
        pygame.display.flip()   # Mets à jour les modifications graphiques

    def _draw_menu(self, model: GameModel) -> None:
        cx = WINDOW_WIDTH // 2

        title_surf = self.font.render(
            "Jeu de course 2D", True, COLOR_ACCENT)
        self.screen.blit(title_surf, title_surf.get_rect(center=(cx, 160)))

        options = [("JOUER (Enter)", GameState.RACING),
                   ("QUITTER (Escape)", None)]
        for i, (label, _) in enumerate(options):
            y = 320 + i * 80
            rect = pygame.Rect(cx - 140, y - 25, 280, 50)
            pygame.draw.rect(self.screen, COLOR_PANEL, rect, border_radius=8)
            pygame.draw.rect(self.screen, COLOR_PANEL_BORDER,
                             rect, 2, border_radius=8)
            text_surf = self.font.render(
                label, True, COLOR_ACCENT if i == 0 else COLOR_TEXT)
            self.screen.blit(text_surf, text_surf.get_rect(center=rect.center))

    def _draw_racing(self, model: GameModel) -> None:
        """Dessine le circuit du jeu.

        Args:
            model (GameModel): class du dossier 'model'
        """

        # Dessine le circuit
        for row_idx, row in enumerate(model.circuit.grid):
            for col_idx, tile in enumerate(row):
                sprite = tile.get_sprite(TILE_SIZE)
                self.screen.blit(
                    sprite, (col_idx * TILE_SIZE, row_idx * TILE_SIZE))

        if model.circuit is None:
            return
        surf, rect = model.car.get_rotated_sprite()
        self.screen.blit(surf, rect)
        
        lap_text = self.font.render(
            f"Tours termines : {model.completed_laps}/{model.required_laps}",
            True,
            COLOR_TEXT,
        )
        self.screen.blit(lap_text, (10, 10))

        if model.race_finished:
            finish_text = self.font.render(
                "Course terminee !",
                True,
                COLOR_ACCENT,
            )
            finish_rect = finish_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            )
            self.screen.blit(finish_text, finish_rect)


    def _draw_circuit_select(self, model: GameModel) -> None:

        title_font = pygame.font.SysFont("Arial", 48, bold=True)
        option_font = pygame.font.SysFont("Arial", 36)

        title = title_font.render(
            "CHOIX DU CIRCUIT",
            True,
            COLOR_ACCENT
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3)
        )

        self.screen.blit(title, title_rect)

        circuits = model.available_circuits

        start_y = WINDOW_HEIGHT // 2

        for i, name in enumerate(circuits):

            color = (
                COLOR_ACCENT
                if i == model.selected_circuit
                else COLOR_TEXT
            )

            prefix = "> " if i == model.selected_circuit else "  "

            text = option_font.render(
                prefix + name,
                True,
                color
            )

            text_rect = text.get_rect(
                center=(WINDOW_WIDTH // 2, start_y + i * 60)
            )

            self.screen.blit(text, text_rect)
