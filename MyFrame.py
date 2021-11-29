from tkinter import Tk, Canvas, Frame, BOTH

from Vector import Vector
class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Вектора")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        #стартовая позиция отрисовки векторов
        START_X = 200
        START_Y = 200

        vector = Vector(0, 100)
        vector2 = Vector(100, 100)
        vector3 = vector.substract_V_From_V(vector2)
        print(vector)
        print(vector2)
        print(vector3)


        #отрисовка векторов
        canvas.create_line(START_X, START_Y,
                           START_X+vector.get_vector()[0], START_Y + vector.get_vector()[1],
                           fill = "red", width = 3)
        canvas.create_line(START_X, START_Y,
                           START_X+vector2.get_vector()[0], START_Y + vector2.get_vector()[1],
                           fill = "green", width = 3)
        canvas.create_line(START_X, START_Y,
                           START_X+vector3.get_vector()[0], START_Y + vector3.get_vector()[1],
                            fill = "blue", width = 3)


        """
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        """
        canvas.pack(fill=BOTH, expand=1)

