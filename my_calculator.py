from tkinter import *


class Calculator:

    def __init__(self, master):
        # This is the string which will hold the main expression to be evaluated.
        self.expression = ''
        self.equation = StringVar()
        self.equation.set('Enter your expression.')

        top_frame = Frame(master)
        top_frame.pack(side=TOP)
        button_grid = Frame(master)
        button_grid.pack(side=BOTTOM)

        self.expression_field = Entry(top_frame, textvariable=self.equation)
        self.expression_field.pack()
        self.expression_field.bind('<Button-1>', self.clear_box)

        self.quit_button = Button(button_grid, text="Quit", command=master.quit)
        self.quit_button.pack(side=RIGHT)

        self.test_button = Button(button_grid, text="What will this be?", command=self.purpose)
        self.test_button.pack(side=LEFT)

    def clear_box(self, _):
        if self.expression_field.get() == 'Enter your expression.':
            self.expression_field.delete(0, END)

    @staticmethod
    def purpose():
        print("I will be a calculator.")


def main():
    calc_root = Tk()
    _ = Calculator(calc_root)
    calc_root.mainloop()


if __name__ == '__main__':
    main()
