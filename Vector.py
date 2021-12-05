import math
from tkinter import Canvas



class Vector:

    """
    За начальную точку координат принимается крайняя верхняя левая точка
    х - вертикаль (сверху вниз)
    у - горизонталь (слева направо)
    чтобы было удобней ориентироваться, удобней будет отразить систему координат по х
    для этого необходимо брать х с отрицательным значением
    """
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = -y



    def add_V_t_V(self, vector_f1):
        vector = Vector(self.__x + vector_f1.get_vector()[0],
                        -(self.__y + vector_f1.get_vector()[1]))
        return vector


    def substract_V_From_V(self, vector_f1):
        vector = Vector(self.__x - vector_f1.get_vector()[0],
                        -(self.__y - vector_f1.get_vector()[1]))
        return vector

    def norma(self) -> float:
        length = math.sqrt(self.__x**2 + self.__y**2)
        return length

    def cos(self, vector):
        """
        scalar - скалярный квадрат вектора (u,v) = u_x*v_x + u_y*v_y
        :param vector:
        :return:
        """
        scalar = self.__x * vector.get_vector()[0] + self.__y * vector.get_vector()[1]
        return scalar / (self.norma() * vector.norma())

    """
    get and set methods
    """

    def get_vector(self):
        return (self.__x, self.__y)

    def set_vector(self, x, y):
        self.__y = y
        self.__x = x



    def __str__(self):
        return f'Vector is x {self.__x}, y {self.__y * -1}'