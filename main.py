# implemented using classes
from tkinter import *

cal = Tk()
cal.title("Smart Calculator")

txtDisplay = Entry(cal, font=('Impact', 20, 'bold'), bd=30, insertwidth=4, bg="powder blue",
                             fg="royal blue",justify='right')
txtDisplay.insert(0, "Let's calculate!")


class Calculator:

    def __init__(self):
        self.output = 0
        self.current = 0
        self.operator = ""
        self.isButton = 0
        self.isRightParen = 0

    def btnClick(self, num):
        if self.isRightParen is 1:
            self.operator = self.operator + "*" + str(num)
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)
            self.expOutput(self.operator)
            self.isButton = 1
            self.isRightParen = 0

        elif self.isRightParen is 0:
            self.operator = self.operator + str(num)
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)
            self.expOutput(self.operator)
            self.isButton = 1
            self.isRightParen = 0

    def leftParenthesesClick(self):

        if self.isRightParen is 1:
            self.operator = self.operator + "*" + "("
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)
            self.isRightParen = 0

        elif self.isButton is 0:
            self.operator = self.operator + "("
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)
            self.isRightParen = 0
        elif self.isButton is 1:
            self.operator = self.operator + "*" + "("
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)
            self.isRightParen = 0

    def rightParenthesesClick(self):
        self.operator = self.operator + ")"
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, self.operator)
        self.expOutput(self.operator)
        self.isRightParen = 1

    def expOutput(self, operator):
        try:
            self.output = str(eval(operator))
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, string=self.operator + "=" + self.output)
            self.current = 0
        except SyntaxError:
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, self.operator)


    def oprtrClick(self, op):
        if self.current is 0:
            self.current = 1
            self.operator = self.operator + op
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, string=self.operator)
            self.isButton = 0
            self.isRightParen = 0
        else:
            self.operator = self.operator + op
            self.isButton = 0
            self.isRightParen = 0
            self.expOutput(self.operator)

    def equals(self):
        self.operator = self.output
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, string=self.operator)

    def clear(self):
        self.__init__()
        txtDisplay.delete(0, END)

    def delete(self):
        self.operator = self.operator[: -1]
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, string=self.operator)


smartCal = Calculator()

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0",
              bg="powder blue", command=lambda: smartCal.btnClick(0))

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1",
              bg="powder blue", command=lambda: smartCal.btnClick(1))

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",
              bg="powder blue", command=lambda: smartCal.btnClick(2))

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",
              bg="powder blue", command=lambda: smartCal.btnClick(3))

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",
              bg="powder blue", command=lambda: smartCal.btnClick(4))

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",
              bg="powder blue", command=lambda: smartCal.btnClick(5))

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",
              bg="powder blue", command=lambda: smartCal.btnClick(6))

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7",
              bg="powder blue", command=lambda: smartCal.btnClick(7))

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8",
              bg="powder blue", command=lambda: smartCal.btnClick(8))

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9",
              bg="powder blue", command=lambda: smartCal.btnClick(9))

btnDecimal = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=".",
                   bg="powder blue", command=lambda: smartCal.btnClick("."))

btnLeftParen = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="(",
                   bg="powder blue", command=smartCal.leftParenthesesClick)

btnRightParen = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=")",
                   bg="powder blue", command=smartCal.rightParenthesesClick)

Add_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+",
                 bg="powder blue", command=lambda: smartCal.oprtrClick("+"))

Sub_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-",
                 bg="powder blue", command=lambda: smartCal.oprtrClick("-"))

Mul_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*",
                 bg="powder blue", command=lambda: smartCal.oprtrClick("*"))

Div_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",
                 bg="powder blue", command=lambda: smartCal.oprtrClick("/"))

btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",
                   bg="powder blue", command=smartCal.equals)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",
                  bg="powder blue", command=smartCal.clear)

btnBackspace = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="⌫",
                  bg="powder blue", command=smartCal.delete)

# {-|-|-|-Positioning-|-|-|-}

txtDisplay.grid(columnspan=4)
# =========================== #
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
Add_btn.grid(row=1, column=3)
# =========================== #
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
Sub_btn.grid(row=2, column=3)
# =========================== #
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
Mul_btn.grid(row=3, column=3)
# =========================== #
btn0.grid(row=4, column=0)
btnClear.grid(row=4, column=1)
btnEquals.grid(row=4, column=2)
Div_btn.grid(row=4, column=3)
# =========================== #
btnDecimal.grid(row=5, column=0)
btnLeftParen.grid(row=5, column=1)
btnRightParen.grid(row=5, column=2)
btnBackspace.grid(row=5, column=3)

cal.mainloop()
