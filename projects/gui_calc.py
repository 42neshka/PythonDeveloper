import tkinter as tk

win = tk.Tk()
win.geometry(f'400x400+1050+350')
win['bg'] = '#e8e8d3'
win.title('Calculator')

# functions

def add_digit(digit):
	value = calc.get()
	if value[0] == '0':
		value = value[1:]
	calc.delete(0, 'end')
	calc.insert('end', value+digit)
 
def add_operation(operation):
	value = calc.get()
	if value[-1] in '+-/*':
		value = value[:-1]
	calc.delete(0, 'end')
	calc.insert('end', value + operation)


def digit_button(digit):
	return tk.Button(win, text=digit, command=lambda : add_digit(digit), font=('Arial', 20), bd=5)
	
def operation_button(operation):
	return tk.Button(win, text=operation, fg='red', command=lambda : add_operation(operation), font=('Arial', 20), bd=5)

def calc_button(calc):
    return tk.Button(win, text=calc, fg='red', command=lambda : add_operation(calc), font=('Arial', 20), bd=5)

# buttons

digit_button('1').grid(row=1, column=0, sticky='wesn', padx=3, pady=3)
digit_button('2').grid(row=1, column=1, sticky='wesn', padx=3, pady=3)
digit_button('3').grid(row=1, column=2, sticky='wesn', padx=3, pady=3)
digit_button('4').grid(row=2, column=0, sticky='wesn', padx=3, pady=3)
digit_button('5').grid(row=2, column=1, sticky='wesn', padx=3, pady=3)
digit_button('6').grid(row=2, column=2, sticky='wesn', padx=3, pady=3)
digit_button('7').grid(row=3, column=0, sticky='wesn', padx=3, pady=3)
digit_button('8').grid(row=3, column=1, sticky='wesn', padx=3, pady=3)
digit_button('9').grid(row=3, column=2, sticky='wesn', padx=3, pady=3)
digit_button('0').grid(row=4, column=0, sticky='wesn', padx=3, pady=3)

operation_button('+').grid(row=1, column=3, sticky='wesn', padx=3, pady=3)
operation_button('-').grid(row=2, column=3, sticky='wesn', padx=3, pady=3)
operation_button('*').grid(row=3, column=3, sticky='wesn', padx=3, pady=3)
operation_button('/').grid(row=4, column=3, sticky='wesn', padx=3, pady=3)

calc_button('=').grid(row=4, column=2, sticky='wesn', padx=3, pady=3)

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=50)
win.grid_columnconfigure(2, minsize=50)
win.grid_columnconfigure(3, minsize=50)
win.grid_columnconfigure(4, minsize=50)
win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=50)
win.grid_rowconfigure(2, minsize=50)
win.grid_rowconfigure(3, minsize=50)
win.grid_rowconfigure(4, minsize=50)


# entries

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20))
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='wens', padx=5, pady=5)

win.mainloop()