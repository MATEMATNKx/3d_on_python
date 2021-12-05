from Vector import Vector
from tkinter import Canvas
class Scene(Canvas):
    def __init__(self,  master=None, cnf={}, **kw):
        """
        got vector and building triangle
        or got points and return vectors if it need
        """

        super(Scene, self).__init__(master, cnf, **kw)

    def draw_triangle(self, ax, ay, bx, by, cx, cy):
        """
        :param заменить значение х и y на ay ax by bx и так далее
        """
        self.create_line(ax, ay, bx, by, fill = 'red', width = 3)
        self.create_line(bx, by, cx, cy, fill = 'blue', width = 3)
        self.create_line(cx, cy, ax, ay, fill = 'black', width = 3)
        "вот тут обновили отрисовку"
        print(ax, ay)
        print(bx, by)
        print(cx, cy)
        params = {}
        params["area"] = 0.5 * abs(((bx - ax) * (cy - ay))\
                                   - ((cx - ax) * (by - ay)))
        return params

    def draw_2dcube(self, centerх, centery, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        :param center: принимает на вход центр квадрата
        дописать код, рисиущий квадрат относительно центра
        пока рисовка происходит относительно начала координат
        """
        x1 += centerх
        y1 += centery
        x2 += centerх
        y2 += centery
        x3 += centerх
        y3 += centery
        x4 += centerх
        y4 += centery
        self.create_line(x1, y1, x2, y2, fill = 'red', width = 3)
        self.create_line(x2, y2, x3, y3, fill = 'blue', width = 3)
        self.create_line(x3, y3, x4, y4, fill = 'black', width = 3)
        self.create_line(x4, y4, x1, y1, fill = 'yellow', width = 3)

    def draw_vector(self, centerx, centery, vector: Vector, color: str):
        """
        :param centerx: start pos_x
        :param centery: start pos_y
        :param vector: class Vector
        :param color: colof for filling
        :return:
        """
        self.create_line(centerx, centery,
                    centerx + vector.get_vector()[0], centery + vector.get_vector()[1],
                    fill=color, width=3)


