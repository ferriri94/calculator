from tkinter import *
from functools import partial
import re


class Calculator:

    def __init__(self, master):
        # This is the string which will hold the main expression to be evaluated.
        self.expression = ''
        self.equation = StringVar()
        self.equation.set('Enter your expression.')

        # Have a previous result value so subsequent calculations can be performed.
        self.ans = 0

        # Create two frames - one for the text box and one for the buttons.
        self.top_frame = Frame(master)
        self.top_frame.pack(side=TOP)
        self.button_grid = Frame(master)
        self.button_grid.pack(side=BOTTOM)

        # Set up the Entry field which will display the expression to be evaluated.
        self.expression_field = Entry(self.top_frame, textvariable=self.equation)
        self.expression_field.pack()
        self.expression_field.bind('<Button-1>', self.__clear_box)

        # Set up all the buttons.
        self.quit_button = Button(self.button_grid, text="Quit", command=master.quit)
        self.quit_button.grid(row=0, column=0)

        self.clear_button = Button(self.button_grid, text="Clear", command=partial(self.__clear_box, 'CLEAR'))
        self.clear_button.grid(row=0, column=1)

        self.del_button = Button(self.button_grid, text="Del", command=self.__trim_expression)
        self.del_button.grid(row=0, column=2)

        self.button1 = Button(self.button_grid, text="1", command=partial(self.__press, 1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.button_grid, text="2", command=partial(self.__press, 2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.button_grid, text="3", command=partial(self.__press, 3))
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.button_grid, text="4", command=partial(self.__press, 4))
        self.button4.grid(row=2, column=0)

        self.button5 = Button(self.button_grid, text="5", command=partial(self.__press, 5))
        self.button5.grid(row=2, column=1)

        self.button6 = Button(self.button_grid, text="6", command=partial(self.__press, 6))
        self.button6.grid(row=2, column=2)

        self.button7 = Button(self.button_grid, text="7", command=partial(self.__press, 7))
        self.button7.grid(row=1, column=0)

        self.button8 = Button(self.button_grid, text="8", command=partial(self.__press, 8))
        self.button8.grid(row=1, column=1)

        self.button9 = Button(self.button_grid, text="9", command=partial(self.__press, 9))
        self.button9.grid(row=1, column=2)

        self.button0 = Button(self.button_grid, text="0", command=partial(self.__press, 0))
        self.button0.grid(row=4, column=1)

        self.dec_point = Button(self.button_grid, text=".", command=partial(self.__press, "."))
        self.dec_point.grid(row=4, column=0)

        self.plus = Button(self.button_grid, text="+", command=partial(self.__press, "+"))
        self.plus.grid(row=3, column=3)

        self.minus = Button(self.button_grid, text="-", command=partial(self.__press, "-"))
        self.minus.grid(row=2, column=3)

        self.times = Button(self.button_grid, text="*", command=partial(self.__press, "*"))
        self.times.grid(row=1, column=3)

        self.divide = Button(self.button_grid, text="/", command=partial(self.__press, "/"))
        self.divide.grid(row=0, column=3)

        self.prev_ans = Button(self.button_grid, text="Ans", command=partial(self.__press, "Ans"))
        self.prev_ans.grid(row=4, column=2)

        self.equals = Button(self.button_grid, text="=", command=self.__evaluate)
        self.equals.grid(row=4, column=3)

        # Finally, associate the enter key with evaluating the expression.
        master.bind('<Return>', self.__evaluate)

    def __clear_box(self, event):
        """
        Function to clear the expression field Entry widget.
        :param event: The event that will trigger this method - checks whether Clear button has been pressed (and hence
                      clear everything not just default message).
        :return: None
        """
        if self.expression_field.get() == 'Enter your expression.' or event == 'CLEAR':
            self.expression = ''
            self.equation.set(self.expression)

    def __trim_expression(self):
        """
        Function to trim final character from expression when Del button is pressed.
        :return: None
        """
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def __press(self, text_to_add):
        """
        Function to augment expression with input from latest button press. Use regex to check if first character of
        expression is an operator, if it is then put previous answer at the start.
        :param text_to_add: Input from button just pressed.
        :return: None
        """
        if not re.search(r'[\w0-9]', self.expression) and type(text_to_add) != int:
            if re.search(r'[^\w\s]', text_to_add):
                self.expression = str(self.ans)
        self.expression += str(self.ans) if text_to_add == "Ans" else str(text_to_add)
        self.equation.set(self.expression)

    def __evaluate(self, _=None):
        """
        Function to evaluate the expression generated from the button presses. Checks for invalid operations and prints
        an error message in the Entry box.
        :param _: Ignored, only present so fn can be called by pressing enter key.
        :return: None
        """
        try:
            self.result = str(eval(self.expression))
            self.ans = self.result
            self.equation.set(self.result)
            self.expression = ''
        except ZeroDivisionError:
            self.equation.set('Math Error: Cannot divide by zero')
            self.expression = ''
        except SyntaxError:
            self.equation.set('Error: Please only use numeric values')
            self.expression = ''


def main():
    """
    Initialise the tkinter context, customise to Calculator class, run GUI.
    :return: None
    """
    calc_root = Tk()
    Calculator(calc_root)
    calc_root.mainloop()


if __name__ == '__main__':
    main()
