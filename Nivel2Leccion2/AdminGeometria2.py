from tkinter import *

class InicioSesion:
    def __init__(self,master):
        self.master = master
        self.DatosUsuario()
        self.Sesion()
        
    def DatosUsuario(self):
        self.marco = Frame(self.master)
        self.marco.place(x = 0, y = 30, width = 225, height = 145)
        
        self.lblUser = Label(self.marco, text = 'Usuario', padx = '10', pady = '5')
        self.lblUser.place(x = 0, y = 30, width = 100, height = 20)
        
        self.lblPass = Label(self.marco, text = 'Contraseña', padx = '10', pady = '5')
        self.lblPass.place(x = 0, y = 80, width = 100, height = 20)
        
        self.entryUser = Entry(self.marco)
        self.entryUser.place(x = 100, y = 30, width = 100, height = 20)
        
        self.entryPass = Entry(self.marco, show="*")
        self.entryPass.place(x = 100, y = 80, width = 100, height = 20)
        
        self.entrar = Button(self.marco, text = 'Entrar', command = self.BusquedaUsuario)
        self.entrar.place(x = 0, y = 120, width = 225, height = 25)   
          
    def Sesion(self):       
        self.marco2 = Frame(self.master)
        self.marco2.place(x = 0, y = 0, width = 225, height = 25)
        
        self.etiqueta = Label(self.marco2)
        self.etiqueta.pack()
        
    def BusquedaUsuario(self):         
        if self.entryUser.get() == 'carlos' and self.entryPass.get() == '123':
            self.etiqueta['text'] = 'Inicio correcto de sesión'
        else:
            self.etiqueta['text'] = 'Usuario o contraseña incorrecto'
        
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)            

root = Tk()
gui = InicioSesion(root)
root.mainloop()