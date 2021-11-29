from tkinter import Tk
from MyFrame import Example
from Vector import Vector
def main():
    root = Tk()

    ex = Example()
    root.geometry("600x400+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()