from tkinter import *
from functools import partial


class Calculator:

    def __init__(self, master):
        # This is the string which will hold the main expression to be evaluated.
        self.expression = ''
        self.equation = StringVar()
        self.equation.set('Enter your expression.')

        # Create two frames - one for the text box and one for the buttons.
        top_frame = Frame(master)
        top_frame.pack(side=TOP)
        button_grid = Frame(master)
        button_grid.pack(side=BOTTOM)

        # Set up the Entry field which will display the expression to be evaluated.
        self.expression_field = Entry(top_frame, textvariable=self.equation)
        self.expression_field.pack()
        self.expression_field.bind('<Button-1>', self.__clear_box)

        # Set up all the buttons.
        self.quit_button = Button(button_grid, text="Quit", command=master.quit)
        self.quit_button.grid(row=0, column=3)

        self.clear_button = Button(button_grid, text="Clear", command=partial(self.__clear_box, 'CLEAR'))
        self.clear_button.grid(row=0, column=2)

        self.button1 = Button(button_grid, text="1", command=partial(self.__press, 1))
        self.button1.grid(row=4, column=0)

        self.button2 = Button(button_grid, text="2", command=partial(self.__press, 2))
        self.button2.grid(row=4, column=1)

        self.button3 = Button(button_grid, text="3", command=partial(self.__press, 3))
        self.button3.grid(row=4, column=2)

        self.button4 = Button(button_grid, text="4", command=partial(self.__press, 4))
        self.button4.grid(row=3, column=0)

        self.button5 = Button(button_grid, text="5", command=partial(self.__press, 5))
        self.button5.grid(row=3, column=1)

        self.button6 = Button(button_grid, text="6", command=partial(self.__press, 6))
        self.button6.grid(row=3, column=2)

        self.button7 = Button(button_grid, text="7", command=partial(self.__press, 7))
        self.button7.grid(row=2, column=0)

        self.button8 = Button(button_grid, text="8", command=partial(self.__press, 8))
        self.button8.grid(row=2, column=1)

        self.button9 = Button(button_grid, text="9", command=partial(self.__press, 9))
        self.button9.grid(row=2, column=2)

        self.button0 = Button(button_grid, text="0", command=partial(self.__press, 0))
        self.button0.grid(row=5, column=1)

        self.dec_point = Button(button_grid, text=".", command=partial(self.__press, "."))
        self.dec_point.grid(row=5, column=0)

    def __clear_box(self, event):
        """
        Function to clear the expression field Entry widget.
        :param event:The event that will trigger this method - checks whether Clear button has been pressed.
        :return:None
        """
        if self.expression_field.get() == 'Enter your expression.' or event == 'CLEAR':
            self.expression = ''
            self.equation.set(self.expression)

    def __press(self, text_to_add):
        self.expression += str(text_to_add)
        self.equation.set(self.expression)


def main():
    # Initialise the tkinter context, customise to Calculator class, run GUI.
    calc_root = Tk()
    Calculator(calc_root)
    calc_root.mainloop()


if __name__ == '__main__':
    main()
