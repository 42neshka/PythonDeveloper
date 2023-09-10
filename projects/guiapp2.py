import tkinter as tk

win = tk.Tk()
win.geometry(f'500x500+1050+350')
win.title('Registration')

# functions

def Entry_button():
    value = name.get()
    if value:
        print(value)
    else:
        print('Incorrect Value')

def Delete_button():
    name.delete(0, 'end')
    password.delete(0, 'end')

def submit_button():
    print(name.get())
    print(password.get())
    Delete_button()


# labels

name_label = tk.Label(win, text='Name: ',
                      font=10)
name_label.grid(row=0, column=0,)

password_label = tk.Label(win, text='Password: ',
                      font=10)
password_label.grid(row=1, column=0,)

# entries

name = tk.Entry(win)
name.grid(row=0, column=1)

password = tk.Entry(win, show='*')
password.grid(row=1, column=1)

# buttons

btn_1 = tk.Button(win, text='Entry',
                  command=Entry_button).grid(row=2, column=0, sticky='we')
btn_2 = tk.Button(win, text='Delete',
                  command=Delete_button).grid(row=2, column=1, sticky='we')
btn_3 = tk.Button(win, text='Insert',
                  command=lambda : name.insert(0, 'wow')).grid(row=2, column=2, sticky='we')
btn_4 = tk.Button(win, text='Submit',
                  command=submit_button).grid(row=0, column=2, sticky='we')


win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=150)
win.grid_columnconfigure(2, minsize=150)

win.mainloop()