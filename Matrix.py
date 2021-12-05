class Matrix:
    __coords = [[0,0],[0,0]]
    __dim = 2
    def __init__(self, coords):
        self.__coords = coords

    def get_dim(self):
        return self.__dim
    def get_coords(self):
        return self.__coords


    def __add__(self, other):
        matrix = Matrix(self.__coords)
        print(other.get_dim())
        for i in range(other.get_dim()):
            for j in range(other.get_dim()):
                matrix.__coords[i][j] += other.get_coords()[i][j]
        return matrix

    def dot_product(self, scalar):
        matrix = self.__coords
        for i in range(self.__dim):
            for j in range(self.__dim):
                matrix[i][j] *= scalar
        matrix = Matrix(matrix)

        return matrix

    def __str__(self):
        string = str(self.__coords)
        return string

a = Matrix([[0, 1], [1, 0]])
b = Matrix([[1, 0], [0, 1]])
print((a+b).dot_product(10))