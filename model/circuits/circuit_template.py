from abc import ABC, abstractmethod

class CircuitTemplate(ABC):
    """
    Classe de base pour tous les circuits.

    Un circuit est défini par un layout textuel où chaque caractère
    représente un type de tuile.
    """
    @property
    @abstractmethod
    def layout(self):
        pass

    @abstractmethod
    def get_tile(self, character, col, row):
        pass

    def create(self):

        grid = []

        for row_idx, row in enumerate(self.layout):

            current_row = []

            for col_idx, cell in enumerate(row):

                current_row.append(
                    self.get_tile(
                        cell,
                        col_idx,
                        row_idx
                    )
                )

            grid.append(current_row)

        return grid