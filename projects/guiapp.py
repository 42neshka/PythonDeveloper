import tkinter as tk

win = tk.Tk()
win.title('love Adeline')
win.geometry('500x500+500+250')
win.minsize(250, 250)
win.maxsize(750, 750)
win.resizable(True, True)
# win.config(bg='grey')

text1 = tk.Label(win, text='''Hello, 
Dear user!''',
				bg='grey',
				fg='white',
				font=('Arial', 15, 'bold'),
				pady=15,
				width=20,
				height=2,
				justify=tk.CENTER,
				anchor='n',
				relief=tk.RAISED,
				bd=5
				)
text1.pack()

win.mainloop()