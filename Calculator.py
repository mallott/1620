from tkinter import *
from CALC_GUI import *


clear_on_text = False
def click_button(number, num_input):
    """I need it so that the number is still accounted for but when another number is inputted
    the input box clears"""
    global clear_on_text
    if clear_on_text:
        num_input.delete(0, END)
        clear_on_text = False
    """button used to add numbers to input box"""
    current_num = num_input.get()
    num_input.delete(0, END)
    num_input.insert(0, current_num + str(number))
    """need num_input to be global"""


def clear_button(num_input):
    global clear_on_text
    num_input.delete(0, END)
    clear_on_text = False

    """Button used to clear any input"""



def calculation(num_input):
    """calculating what has been put into the input box"""
    global clear_on_text
    try:
        expression = num_input.get()
        expression = expression.replace('x', '*')
        result = eval(expression)
        """need to check if number is int or not"""
        if isinstance(result,float) and result.is_integer():
            result = int(result)
        num_input.delete(0, END)
        num_input.insert(0, str(result))
        clear_on_text = True
    except Exception:
        num_input.delete(0, END)
        num_input.insert(0, 'Error')
        clear_on_text = True


def percentage_sign(num_input):
    """when user clicks the comp will treat the number as a percentage"""
    try:
        value = float(num_input.get())
        num_input.delete(0, END)
        num_input.insert(0, str(value/100))
    except Exception:
        num_input.delete(0, END)
        num_input.insert(0, 'Error')


def toggle_sign(num_input):
    """make input neg if wanted"""
    try:
        value = float(num_input.get())
        value = int(-value)
        num_input.delete(0, END)
        num_input.insert(0, str(value))
    except Exception:
        num_input.delete(0, END)
        num_input.insert(0, 'Error')
def del_button(num_input):
    """backspace button"""
    current = num_input.get()
    num_input.delete(0, END)
    num_input.insert(0, current[:-1])


"""https://intellij-support.jetbrains.com/hc/en-us/community/posts/360009445239-Python-Tkinter-Calculator"""



if __name__ == '__main__':
    main()
