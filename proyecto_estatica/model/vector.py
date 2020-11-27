from dataclasses import dataclass
from model.punto import Punto

from math import cos


@dataclass
class Vector:
    fuerza: Punto

    @classmethod
    def from_magnitud_cosenos(cls,
                              magnitud: float,
                              alfa: float,
                              beta: float,
                              gamma: float):
        return cls(
            Punto(
                magnitud * cos(alfa),
                magnitud * cos(beta),
                magnitud * cos(gamma)
            )
        )

    @classmethod
    def from_vector_cartesiano(cls, Vector):
        return cls(Vector)

    @classmethod
    def from_magnitud_direccion(cls,
                                magnitud: float,
                                p1: Punto,
                                p2: Punto):
        pass

    def __str__(self):
        return f'Vector({round(self.fuerza.x, 2)}i' \
            f'+ {round(self.fuerza.y, 2)}j' \
            f'+ {round(self.fuerza.z, 2)}k)'
