from tkinter import*

def btnClick(numbers):
    global operator  # https://www.geeksforgeeks.org/global-local-variables-python/
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set(operator)

def btnEqualsOutput():
    global operator
    output = str(eval(operator))
    text_input.set(output)
    operator = output

def btnBackspace():
    global operator
    operator = operator[: -1]  # remove last character from string
    text_input.set(operator)

cal = Tk()
cal.title("Smart Calculator")

operator = ""
text_input = StringVar()  # It's not possible to hand over a regular Python variable to a widget through a variable or
                          #  textvariable option. The only kinds of variables for which this works are variables that
                          # are subclassed from a class called Variable, defined in the Tkinter module.
"""
Defining the display box. Entry widget allows the user to enter a single line of text.
1st arg: represents the parent window, where the entry widget should be placed.
textvariable: In order to be able to retrieve the current text from your entry widget, 
you must set this option to an instance of the StringVar class.
insertwidth: Width of the insertion cursor
 
"""
txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue",
                             justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7",
              bg="powder blue", command=lambda: btnClick(7)).grid(row=1, column=0)  # use lambda when function has arguments. otherwise, w/o lambda

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8",
              bg="powder blue", command=lambda: btnClick(8)).grid(row=1, column=1)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9",
              bg="powder blue", command=lambda: btnClick(9)).grid(row=1, column=2)

Add_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+",
                 bg="powder blue", command=lambda: btnClick("+")).grid(row=1, column=3)

# =======================================================================================================================

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",
              bg="powder blue", command=lambda: btnClick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",
              bg="powder blue", command=lambda: btnClick(5)).grid(row=2, column=1)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",
              bg="powder blue", command=lambda: btnClick(6)).grid(row=2, column=2)

Sub_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-",
                 bg="powder blue", command=lambda: btnClick("-")).grid(row=2, column=3)

# =======================================================================================================================

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1",
              bg="powder blue", command=lambda: btnClick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",
              bg="powder blue", command=lambda: btnClick(2)).grid(row=3, column=1)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",
              bg="powder blue", command=lambda: btnClick(3)).grid(row=3, column=2)

Mul_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*",
                 bg="powder blue", command=lambda: btnClick("*")).grid(row=3, column=3)

# =======================================================================================================================

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0",
              bg="powder blue", command=lambda: btnClick(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",
                  bg="powder blue", command=btnClearDisplay).grid(row=4, column=1)

btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",
                   bg="powder blue", command=btnEqualsOutput).grid(row=4, column=2)

Div_btn = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",
                 bg="powder blue", command=lambda: btnClick("/")).grid(row=4, column=3)

# =======================================================================================================================

btnLeftParentheses = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="(",
              bg="powder blue", command=lambda: btnClick("(")).grid(row=5, column=0)

btnRightParentheses = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=")",
                  bg="powder blue", command=lambda: btnClick(")")).grid(row=5, column=1)

btnDecimal = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text=".",
                   bg="powder blue", command=lambda: btnClick(".")).grid(row=5, column=2)

btnBackspace = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Delete",
                 bg="powder blue", command=btnBackspace).grid(row=5, column=3)

cal.mainloop()