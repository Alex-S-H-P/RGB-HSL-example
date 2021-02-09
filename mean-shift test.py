import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


class Point:

    def __init__(self, pos: list):
        self.pos = pos

    @classmethod
    def random(cls, dim: int = 2):
        pos = []
        for _ in range(dim):
            pos.append(np.random.normal())
        return cls(pos)

    @staticmethod
    def getcoord(i: int, this_universe) -> list:
        return [this_universe[j].pos[i] for j in range(len(this_universe))]

    def within(self, LookUp_range: float):
        w = []
        for point in universe:
            if self.dist(point) < LookUp_range:
                w.append(point)
        return w

    def dist(self, pointB):
        return sqrt(sum([(self.pos[i] - pointB.pos[i]) ** 2 for i in range(len(self.pos))]))

    def move(self, radius):
        mini_verse = self.within(radius)
        dim = len(self.pos)
        vector = [0] * dim
        for i in range(dim):
            vector[i] = sum(Point.getcoord(i, mini_verse)) / len(mini_verse)
        ## draw the vector
        X = (self.pos[0], vector[0])
        Y = (self.pos[1], vector[1])
        plt.plot(X, Y, "b")
        plt.draw()
        ## Update position
        self.pos = vector

nb_desired = 150
universe = [Point.random() for _ in range(nb_desired)]
plt.plot(Point.getcoord(0, universe),
         Point.getcoord(1, universe),
         "ro")
plt.draw()
plt.pause(4)
LookUpRange = 1.1
index = np.random.randint(0, len(universe))
pointer = Point(universe[index].pos)
for _ in range(20):
    circle = plt.Circle(xy=(pointer.pos[0], pointer.pos[1]),
                        radius=LookUpRange)
    plt.gca().add_patch(circle)
    pointer.move(LookUpRange)
    plt.draw()
    plt.pause(0.1)
    print(_)
