from tkinter import *

def mostrarSaludo(event):
    saludo['text'] = 'Hola, ' + nombre.get()

root = Tk()
nombre = Entry(root)
saludo = Label(root)
nombre.pack()
saludo.pack()
nombre.bind('<Key-Return>', mostrarSaludo)
root.mainloop()