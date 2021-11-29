from Vector import Vector
from tkinter import Canvas
class Triangle(Canvas):
    def __init__(self,  master=None, cnf={}, **kw):
        """
        got vector and building triangle
        or got points and return vectors if it need
        """

        super(Triangle, self).__init__(master, cnf, **kw)

    def draw_triangle(self, x1, y1, x2, y2, x3, y3):
        """
        :param заменить значение х и y на ay ax by bx и так далее
        """
        self.create_line(x1, y1, x2, y2, fill = 'red', width = 3)
        self.create_line(x2, y2, x3, y3, fill = 'blue', width = 3)
        self.create_line(x3, y3, x1, y1, fill = 'black', width = 3)
        "вот тут обновили отрисовку"
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)
        params = {}
        params["area"] = 0.5 * abs(((x2 - x1) * (y3 - y1))\
                                   - ((x3 - x1) * (y2 - y1)))
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


