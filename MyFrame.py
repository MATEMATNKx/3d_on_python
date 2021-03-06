import math
import time
from tkinter import Tk, Canvas, Frame, BOTH

from Vector import Vector
from Scene import Scene
from Matrix import Matrix

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Векторая графика")
        self.pack(fill=BOTH, expand=1)



        #стартовая позиция отрисовки векторов
        START_X = 250
        START_Y = 250
        fi = [0.1]
        #convert list to matrix
        basis = [[1, 0], [0, 1]]
        basis = basis
        scene = Scene(self)
        scene.pack(fill=BOTH, expand=1)

        def callback(event):
            scene.delete("all")
            basis[0][0] += 0.1
            basis[1][1] += 0.1
            draw(basis)

        def callback2(event):
            scene.delete("all")
            basis[0][0] -= 0.1
            basis[1][1] -= 0.1
            draw(basis)

        def reflect_x(event):
            scene.delete("all")
            basis[0][0] = -basis[0][0]
            draw(basis)
        def reflect_y(event):
            scene.delete("all")
            basis[1][1] = -basis[1][1]
            draw(basis)

        def rotation_fi(event):
            scene.delete("all")
            """
            basis[0][0] = math.cos(fi[0])
            basis[0][1] = math.sin(0.1)
            basis[1][0] = -math.sin(0.1)
            basis[1][1] = math.cos(0.1)
            прикольный эффект
            """
            basis[0][0] = math.cos(fi[0])
            basis[0][1] = math.sin(fi[0])
            basis[1][0] = -math.sin(fi[0])
            basis[1][1] = math.cos(fi[0])
            fi[0]+=0.1
            draw(basis)

        scene.bind("<Left>",rotation_fi)
        scene.bind("<x>", reflect_x)
        scene.bind("<y>", reflect_y)
        scene.bind("<Button-1>", callback)
        scene.bind("<Button-3>", callback2)

        scene.focus_set()

        def draw(basis):
            vector = Vector(50, 0)
            scene.draw_vector(START_X - 100, START_Y - 100, vector, 'red', basis)
            vector2 = Vector(0, 50)
            scene.draw_vector(START_X - 100, START_Y - 100, vector2, "blue", basis)
            vector3 = vector.add_V_t_V(vector2)
            scene.draw_vector(START_X - 100, START_Y - 100, vector3, "black", basis)
            vector4 = vector.substract_V_From_V(vector2)
            scene.draw_vector(START_X - 100, START_Y - 100, vector4, "yellow", basis)

        """"<Button-2>"
        метод triangle на вход принимает вектора и отрисовывает их
        более подробней разобраться как работается эта штука.
        В теории всё оперируется точками и векторами
        Ещё бы научиться правильно пользоваться гитом
        """
        area = scene.draw_triangle(START_X + 50, START_Y + 0,
                               START_X + 0, START_Y + 50,
                               START_X + 0, START_Y + 0)

        print(f"area of triangle is {area['area']}")
        scene.draw_2dcube(START_X+ 100, START_Y- 100,
                             0, 100,
                             100, 100,
                             100, 0,
                             0, 0)

        vector = Vector(50,0)
        scene.draw_vector(START_X-100, START_Y-100, vector, 'red', basis)
        vector2 = Vector(0,50)
        scene.draw_vector(START_X - 100, START_Y - 100, vector2, "blue", basis)
        print(f'cos red, blue vectors is:{vector.cos(vector2)}')
        vector3 = vector.add_V_t_V(vector2)
        scene.draw_vector(START_X - 100, START_Y - 100, vector3, "black",basis)
        print(f'cos blue, black vectors is:{vector2.cos(vector3)}')
        print(f'cos black, blue vectors is:{vector3.cos(vector2)}')
        vector4 = vector.substract_V_From_V(vector2)
        scene.draw_vector(START_X - 100, START_Y - 100, vector4, "yellow",basis)
        print(f'cos black, black vectors is:{vector3.cos(vector3)}')
        #scene.pack(fill=BOTH, expand=1)
        #scene.delete("all")
        #scene.draw_vector(START_X-100, START_Y-100, vector, 'red', basis)



        time.sleep(1)



        '''
        vector = Vector(0, 100)
        vector2 = Vector(100, 100)
        print(vector)
        print(vector2)

        print(f'Substract vector {vector} from vector {vector2}')
        vector3 = vector.substract_V_From_V(vector2)
        print(vector3)
        vector4 = vector.add_V_t_V(vector2)
        print(f'Add vector {vector} to vector {vector2}')
        print(vector4)

        #отрисовка векторов
        canvas = Canvas(self)
        canvas.create_line(START_X, START_Y,
                           START_X+vector.get_vector()[0], START_Y + vector.get_vector()[1],
                           fill = "red", width = 3)
        canvas.create_line(START_X, START_Y,
                           START_X+vector2.get_vector()[0], START_Y + vector2.get_vector()[1],
                           fill = "green", width = 3)
        canvas.create_line(START_X, START_Y,
                           START_X+vector3.get_vector()[0], START_Y + vector3.get_vector()[1],
                            fill = "blue", width = 3)
        canvas.create_line(START_X, START_Y,
                           START_X+vector4.get_vector()[0], START_Y + vector4.get_vector()[1],
                            fill = "black", width = 3)
        
        canvas.pack(fill=BOTH, expand=1)
        '''
