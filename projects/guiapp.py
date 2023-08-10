import tkinter as tk
import random

win = tk.Tk()
win.title('Graphical User Interface')
win.geometry('500x500+500+250')
win.minsize(250, 250)
win.maxsize(750, 750)
win.resizable(True, True)
# win.config(bg='grey')

# counter = 0

# def say_hello():
# 	print('Hello, name!')

# def add_label():
# 	label = tk.Label(win, text='new label')
# 	label.pack()

# def button_counter():
# 	global counter
# 	counter += 1
# 	btn4['text'] = f'Счетчик: {counter}'

# def change_color():
# 	win.config(bg=f"#{random.randrange(0x1000000):06x}")

# def deactivate():
# 	if btn4['state'] == tk.DISABLED:
# 		btn4['state'] = tk.NORMAL
# 	else:
# 		btn4['state'] = tk.NORMAL
	 

# text1 = tk.Label(win, text='''Hello, 
# Dear user!''',
# 				bg='grey',
# 				fg='white',
# 				font=('Arial', 15, 'bold'),
# 				pady=15,
# 				width=20,
# 				height=2,
# 				justify=tk.CENTER,
# 				anchor='n',
# 				relief=tk.RAISED,
# 				bd=5
# 				)
# text1.pack()

# btn1 = tk.Button(win, text='Unlock counter',
# 				#  command=say_hello,
# 				 command=deactivate
# 				 )

# btn2 = tk.Button(win, text='Add new Label')

# btn3 = tk.Button(win, text='Add new Label lambda',
# 				 command=lambda: tk.Label(win, text='new lambda').pack())

# btn4 = tk.Button(win, text=f'Счетчик: {counter}',
# 				command=button_counter,
# 				font=('Arial', 10, 'bold'),
# 				bg='grey',
# 				fg='white',
# 				activebackground='white',
# 				state=tk.DISABLED)

# btn5 = tk.Button(win, text='Change background color',
# 				 command=change_color)

btn6 = tk.Button(win, text='test grid')
btn7 = tk.Button(win, text='test grid')
btn8 = tk.Button(win, text='test grid')
btn9 = tk.Button(win, text='test grid')
btn10 = tk.Button(win, text='test grid')
btn11 = tk.Button(win, text='test grid')
btn12 = tk.Button(win, text='test grid')


# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()
# btn5.pack()
btn6.grid(row=0, column=0)
btn7.grid(row=1, column=1)
btn8.grid(row=2, column=2)
btn9.grid(row=4, column=1)
btn10.grid(row=5, column=2)
btn11.grid(row=6, column=3)
btn12.grid(row=7, column=4)

win.mainloop()