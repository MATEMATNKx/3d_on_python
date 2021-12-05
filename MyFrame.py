from tkinter import Tk, Canvas, Frame, BOTH

from Vector import Vector
from Scene import Scene
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

        scene = Scene(self)

        """
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
        scene.draw_vector(START_X-100, START_Y-100, vector, 'red')
        vector2 = Vector(0,50)
        scene.draw_vector(START_X - 100, START_Y - 100, vector2, "blue")
        print(f'cos red, blue vectors is:{vector.cos(vector2)}')
        vector3 = vector.add_V_t_V(vector2)
        scene.draw_vector(START_X - 100, START_Y - 100, vector3, "black")
        print(f'cos blue, black vectors is:{vector2.cos(vector3)}')
        print(f'cos black, blue vectors is:{vector3.cos(vector2)}')
        vector4 = vector.substract_V_From_V(vector2)
        scene.draw_vector(START_X - 100, START_Y - 100, vector4, "yellow")
        print(f'cos black, black vectors is:{vector3.cos(vector3)}')
        scene.pack(fill=BOTH, expand=1)



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
