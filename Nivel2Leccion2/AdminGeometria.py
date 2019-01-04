from tkinter import *

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.crearWidgets()
        self.master.geometry("600x300")
        
    def crearWidgets(self):
        self.etiqueta = Label(self.master, cursor = "pencil", fg = "red", bg = "white",
                 text = """Texto de la etiqueta. Si ocupa varios renglones,
poner doble comilla triple al escribir la cadena""",
                 font  = ("Times", "12", "italic"))
        self.etiqueta.pack(side = 'left')
        
        self.boton = Button(self.master, text = "Cerrar ventana", command = self.master.quit)
        self.boton.pack(side = 'bottom', padx = '20', ipady = '25')
        
        self.etiqueta2 = Label(text = 'Hola Mundo')
        self.etiqueta2.pack()



#Creación de la ventana raíz de la GUI
root = Tk()

#root.minsize(300, 300)
#root.maxsize(900, 900)
#root.geometry("900x300")
root.title("Mi Primera Interfaz")

gui = Interfaz(root)
root.mainloop()



"""from tkinter import *

class InicioSesion:
    def __init__(self,master):
        self.master = master
        self.DatosUsuario()
        self.Sesion()
        
    def DatosUsuario(self):
        self.marco = Frame(self.master)
        self.marco.grid(row = 1, column = 0)
        
        self.lblUser = Label(self.marco, text = 'Usuario', padx = '10', pady = '5')
        self.lblUser.grid(column = 0, row = 0)
        
        self.lblPass = Label(self.marco, text = 'Contraseña', padx = '10', pady = '5')
        self.lblPass.grid(column = 0, row = 1)
        
        self.entryUser = Entry(self.marco)
        self.entryUser.grid(column = 1, row = 0)
        
        self.entryPass = Entry(self.marco, show="*")
        self.entryPass.grid(column = 1, row = 1)
        
        self.entrar = Button(self.marco, text = 'Entrar', command = self.BusquedaUsuario)
        self.entrar.grid(column = 0, row = 2, columnspan = 2, sticky = 'ew')   
        
    def Sesion(self):       
        self.marco2 = Frame(self.master, pady = '20')
        self.marco2.grid(column = 0, row = 0)
        
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
root.mainloop()"""