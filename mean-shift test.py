import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from matplotlib import animation, rc
from matplotlib.animation import PillowWriter

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
        # plt.plot(X, Y, "b")
        # plt.draw()
        ## Update position
        self.pos = vector


# equivalent to rcParams['animation.html'] = 'html5'
rc('animation', html='html5')
fig, ax = plt.subplots()

fig.set_size_inches(5,5)
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))
print(ax.__class__.__name__)

line, = ax.plot([], [], lw=2)
nb_desired = 150
universe = [Point.random() for _ in range(nb_desired)]
LookUpRange = 1.1


def get_universe():
    UN = [ax.plot([], [], ls=None, marker="o", color="red")[0] for _ in range(nb_desired)]
    UN.append(ax.plot([], [], ls=None, marker="o", color="black")[0])
    global pointer
    pointer = Point([2, 2])
    universe.append(pointer)
    UN.append(ax.plot([], [], color="blue")[0])
    global circle
    circle = plt.Circle(xy=(pointer.pos[0], pointer.pos[1]),
                        radius=LookUpRange)
    UN.append(circle)
    UN.append(ax.plot([], [], color="black")[0])
    return tuple(UN)


universe_to_draw = get_universe()


# animation function. This is called sequentially
def animate(k):
    for i in range(nb_desired + 1):
        pos = universe[i].pos
        universe_to_draw[i].set_data(pos[0], pos[1])
    mem = pointer.pos[:]
    pointer.move(LookUpRange)
    new = pointer.pos
    circle.center = pointer.pos
    ax.add_patch(circle)
    vector = universe_to_draw[-1]
    X = [mem[0], new[0]]
    Y = [mem[1], new[1]]
    vector.set_data(X, Y)
    return universe_to_draw


# call the animator. blit=True means only re-draw the parts that
# have changed.
anim = animation.FuncAnimation(fig, animate,
                               frames=15, interval=250, blit=True)

writer = PillowWriter(fps=25)
anim.save('myAnimation.gif', writer)
plt.show()
#
# universe = [Point.random() for _ in range(nb_desired)]
# plt.plot(Point.getcoord(0, universe),
#         Point.getcoord(1, universe),
#         "ro")
# plt.draw()
# plt.pause(4)
# LookUpRange = 1.1
# index = np.random.randint(0, len(universe))
# pointer = Point(universe[index].pos)
# for _ in range(20):
#    circle = plt.Circle(xy=(pointer.pos[0], pointer.pos[1]),
#                        radius=LookUpRange)
#    plt.gca().add_patch(circle)
#    pointer.move(LookUpRange)
#    plt.draw()
#    plt.pause(0.1)
#    print(_)
