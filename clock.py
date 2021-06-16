from tkinter import *
from tkinter.ttk import *
from time import strftime
tk=Tk()
tk.title('Clock')
def time():
    text=strftime('%H:%M:%S %p')
    label.config(text=text)
    label.after(1000, time)

label = Label(tk, font=('ds-digital', 40, 'bold'), background='black', foreground='green2')
label.pack(anchor='center')
time()
mainloop()