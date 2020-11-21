from model.vector import Vector


class Vectores:
    vectores = []

    def __init__(self):
        self.vectores = []

    def addVector(self, vector: Vector):
        self.vectores.append(vector)

    def vector_resultante(self):
        return self.vectores
