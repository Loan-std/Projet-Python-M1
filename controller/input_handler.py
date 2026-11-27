import pygame


MAPPING_P1 = {
    pygame.K_UP:     "accelerate",
    pygame.K_DOWN:   "braking",
    pygame.K_LEFT:   "turn_left",
    pygame.K_RIGHT:  "turn_right"
}

MAPPING_P2 = {
    pygame.K_z:   "accelerate",
    pygame.K_s:   "braking",
    pygame.K_q:   "turn_left",
    pygame.K_d:   "turn_right"
}


class InputHandler:

    def __init__(self):
        self.mapping_p1 = MAPPING_P1
        self.mapping_p2 = MAPPING_P2

    def get_inputs(self, mapping) -> dict:
        """Récupère les inputs et leur actions associées si il y en a.

        Returns:
            dict: Dictionnaire des actions qu'il est possible d'effectuer
        """
        # Récupère la touche pressée
        keys = pygame.key.get_pressed()
        # dictionnaire avec les actions
        p = {action: False for action in mapping.values()}

        # Si la touche pressée est dans MAPPING alors l'action vaudra True
        for key, action in mapping.items():
            if keys[key]:
                p[action] = True

        return p

    def get_player1_inputs(self):
        return self.get_inputs(self.mapping_p1)

    def get_player2_inputs(self):
        return self.get_inputs(self.mapping_p2)
