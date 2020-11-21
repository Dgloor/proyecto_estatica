from dataclasses import dataclass


@dataclass
class Punto:
    x: float
    y: float
    z: float

    def __add__(self, other):
        return Punto(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z)