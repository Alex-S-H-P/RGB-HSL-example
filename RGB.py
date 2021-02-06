import tkinter as tk
import numpy as np
import colorsys


class Point:
    def __init__(self, x, y, z, color=None):
        self.pos = [x, y, z]
        self.color = [x, y, z]

    def map(self) -> [float]:
        return map(self.pos)

    @staticmethod
    def hsv2rgb(h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

    def getHex(self):
        return "#%02x%02x%02x" % (self.color[0], self.color[1], self.color[2])

    def display(self, canvas: tk.Canvas):
        R = 5
        x1, y1 = self.map()
        x2, y2 = self.map()
        x1 -= R
        x2 += R
        y1 -= R
        y2 += R
        canvas.create_oval(x1, y1, x2, y2, fill="{}".format(self.getHex()))


def map(coords: [float]) -> [float]:
    x = coords[0]
    y = coords[1]
    z = coords[2]
    x = x + z * zx
    y = y + z * zy
    return np.array([x, y])


def display(points: [Point], canvas: tk.Canvas) -> None:
    for point in points:
        point.display(canvas=canvas)


if __name__ == "__main__":
    root = tk.Tk()
    zx = 0.5
    zy = 0.5
    cv = tk.Canvas(master=root, bg="white", height=512, width=512)
    points: [Point] = []
    for _x in range(0, 255, 15):
        for _y in range(0, 255, 15):
            for _z in range(0, 255, 15):
                point = Point(_x , _y , _z)
                point.pos = [point.pos[i] + 64 for i in range (3)]
                points.append(point)
    print(len(points))
    display(points, canvas=cv)
    cv.pack()
    root.mainloop()
    del root
    ###################################################################
    zx = .3333
    zy = 0
    root = tk.Tk()
    cv = tk.Canvas(master=root, bg="white", height=512, width=512)
    points: [Point] = []
    OffsetZ = 0
    offsetX = 64 + 32
    offsetY = 64 + 32
    for theta in range(0, 90, 10):
        for _z in range(100, 0, -10):
            for r in range(0, 100, 10):
                point = Point(2*(r * np.cos(np.pi / 180 * theta) + offsetX),
                              2*(r * np.sin(np.pi / 180 * theta)  + offsetY),
                              2*(_z + OffsetZ))
                point.color = list(Point.hsv2rgb(theta/360, r/100, _z/100))
                points.append(point)
    for theta in range(90, 180, 10):
        for r in range(0, 100, 10):
            for _z in range(0, 100, 10):
                point = Point(2*(r * np.cos(np.pi / 180 * theta) + offsetX),
                              2*(r * np.sin(np.pi / 180 * theta)  + offsetY),
                              2*(_z + OffsetZ))
                point.color = list(Point.hsv2rgb(theta/360, r/100, _z/100))
                points.append(point)
    for theta in range(360, 270, -10):
        for _z in range(0, 100, 10):
            for r in range(0, 100, 10):
                point = Point(2*(r * np.cos(np.pi / 180 * theta) + offsetX),
                              2*(r * np.sin(np.pi / 180 * theta)  + offsetY),
                              2*(_z + OffsetZ))
                point.color = list(Point.hsv2rgb(theta/360, r/100, _z/100))
                points.append(point)
    for theta in range(270, 170, -10):
        for r in range(0, 100, 10):
            for _z in range(0, 100, 10):
                point = Point(2*(r * np.cos(np.pi / 180 * theta) + offsetX),
                              2*(r * np.sin(np.pi / 180 * theta)  + offsetY),
                              2*(_z + OffsetZ))
                point.color = list(Point.hsv2rgb(theta/360, r/100, _z/100))
                points.append(point)


    print(len(points))
    display(points, canvas=cv)
    cv.pack()
    root.mainloop()
    print("-As")
