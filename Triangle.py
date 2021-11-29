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
        self.create_line(x1, y1, x2, y2, fill = 'red', width = 3)
        self.create_line(x2, y2, x3, y3, fill = 'blue', width = 3)
        self.create_line(x3, y3, x1, y1, fill = 'black', width = 3)
        "вот тут обновили отрисовку"
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)

