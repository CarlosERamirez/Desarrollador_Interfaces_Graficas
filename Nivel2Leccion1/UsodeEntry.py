from tkinter import *

class InicioSesion:
    def __init__(self,master):
        self.master = master
        self.marcoIngreso()
        self.marcoSalida()
        self.master.geometry("300x120")
        
    def marcoIngreso(self):
        self.marco = Frame(self.master, pady = '20')
        self.marco.pack()
        
        self.etiqueta = Label(self.marco, text = 'Contraseña')
        self.etiqueta.pack(side = 'left')
        
        self.contrasena = Entry(self.marco, show="*")
        self.contrasena.pack(side = 'left')  
        self.contrasena.bind('<Key-Return>', self.mostrarSalida)
        
        
    def marcoSalida(self):       
        self.marco2 = Frame(self.master, pady = '20')
        
        self.etiqueta2 = Label(self.marco2)
        self.etiqueta2.pack()
        
    def mostrarSalida(self, event):
        self.contenido = self.contrasena.get()
        self.contrasena.delete(0,END)
         
        if self.contenido == 'carlos':
            self.etiqueta2['text'] = 'Contraseña correcta'
        else:
            self.etiqueta2['text'] = 'Contraeña incorrecta'
        self.marco2.pack()
    

root = Tk()
gui = InicioSesion(root)
root.mainloop()