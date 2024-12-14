

from tkinter import Entry

from Calculator import *


def main():
    """General window frame"""
    window = Tk()
    window.title('Calculator Project')
    window.geometry('390x610')
    window.resizable(False, False)

    """input box"""

    num_input: Entry = Entry(window, width=25, borderwidth=0, font=('Arial', 20))
    num_input.grid(row=0, column=0, columnspan=50, padx=35, pady=35, ipady=70)

    """number buttons, make list?"""
    button_display = [
        ('AC', 1, 1), ('+/-', 1, 2), ('%', 1, 3), ('/', 1, 4),
        ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('x', 2, 4),
        ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('-', 3, 4),
        ('1', 4, 1), ('2', 4, 2), ('3', 4, 3), ('+', 4, 4),
        ('DEL', 5, 1), ('0', 5, 2), ('.', 5, 3), ('=', 5, 4)
    ]
    """the equal sign is not displaying on the keyboard but when I put a different character like 'i' 
    its will display"""

    """button display"""
    for (text, row, col) in button_display:
        if text == '=':
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda: calculation(num_input))
            button.grid(row=row, column=col)
            """I didn't put = in the if portion, now the sign displays"""
        elif text == 'AC':
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda: clear_button(num_input))
            button.grid(row=row, column=col)
        elif text == '%':
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda: percentage_sign(num_input))
            button.grid(row=row, column=col)
        elif text == '+/-':
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda: toggle_sign(num_input))
            button.grid(row=row, column=col)
        elif text == 'DEL':
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda: del_button(num_input))
            button.grid(row=row, column=col)
        else:
            button = Button(window, text=text, pady=20, padx=20, font=('Arial', 20),
                            command=lambda t=text: click_button(t, num_input) )
            button.grid(row=row, column=col)

    window.mainloop()
