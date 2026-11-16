import pygame


MAPPING = {
    pygame.K_UP:     "accelerate",
    pygame.K_DOWN:   "braking",
}


class InputHandler:

    def __init__(self):
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        """Récupère les inputs et leur actions associées si il y en a.

        Returns:
            dict: Dictionnaire des actions qu'il est possible d'effectuer
        """
        # Récupère la touche pressée
        keys = pygame.key.get_pressed()
        # dictionnaire avec les actions
        p = {action: False for action in self.mapping.values()}

        # Si la touche pressée est dans MAPPING alors l'action vaudra True
        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p
