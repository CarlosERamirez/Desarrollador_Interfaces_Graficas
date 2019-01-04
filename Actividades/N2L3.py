from tkinter import *
from PIL import ImageTk

class interfazMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido al restaurante")
        self.root.minsize(400, 300)
        self.Lplatillo = [["pollo", 20], ["pescado", 30], ["res", 25]]
        self.Lbebida = [["agua", 5], ["jugo", 10], ["refresco", 10]]
        #orden y cuenta
        self.orden = []
        self.costo = 0
        self.imprimirMenu()
    
    def imprimirMenu(self):
        #barra de menú
        self.root.option_add('*tearOff', FALSE)
        barradeMenu = Menu(self.root)   
        barradeMenu.add_command(label = "Nueva orden", command = self.nuevaOrden)
        self.root.config(menu=barradeMenu)
        
        #imagen
        imagen = ImageTk.PhotoImage(file = 'C:/Users/Carlos Ramirez/Desktop/pasta.png')
        lblImagen = Label(self.root, image = imagen)
        lblImagen.pack()
        lblImagen.image = imagen
        
        #Frame
        self.marco1 = Frame(self.root)
        self.marco1.pack()
        
        #Nombre cliente
        self.lblCliente = Label(self.marco1, text = "Cliente", font  = ("Times", "15", "italic"))
        self.lblCliente.grid(row = 0, column = 0, sticky = 'ew')
        self.nombre = Entry(self.marco1)
        self.nombre.grid(row = 0, column = 1, sticky = 'ew', columnspan = 2)
        
        #Concepto y costo
        self.lblConcepto = Label(self.marco1, text = "Concepto", font  = ("Times", "15", "italic"))
        self.lblConcepto.grid(row = 1, column = 1, sticky = 'ew')
        self.lblCosto = Label(self.marco1, text = "Costo", font  = ("Times", "15", "italic"))
        self.lblCosto.grid(row = 1, column = 2, sticky = 'ew')
        
        #Platillo
        self.lblPlatillo = Label(self.marco1, text = "Platillo", font  = ("Times", "15", "italic"))
        self.lblPlatillo.grid(row = 2, column = 0, sticky = 'ew')
        
        #listas para almacenar botones de platillos
        self.casillas = []
        self.casillas2 = []
        
        #contador para aumentar índice de listas
        k = 0 
        for elemento in self.Lplatillo:
            self.casillas.append(Button(self.marco1, text = str(elemento[0]), command = lambda e = k: self.cuenta('a', e)))
            self.casillas2.append(Label(self.marco1, text = str(elemento[1])))
            self.casillas[k].grid(row = k + 2, column = 1, sticky = 'ew')
            self.casillas2[k].grid(row = k + 2, column = 2, sticky = 'ew')
            k += 1
        
        #Bebida
        self.lblBebida = Label(self.marco1, text = "Bebida", font  = ("Times", "15", "italic"))
        self.lblBebida.grid(row = k + 2, column = 0, sticky = 'ew')
        
        for elemento in self.Lbebida:
            self.casillas.append(Button(self.marco1, text = str(elemento[0]), command = lambda e = k: self.cuenta('b', e)))
            self.casillas2.append(Label(self.marco1, text = str(elemento[1])))
            self.casillas[k].grid(row = k + 2, column = 1, sticky = 'ew')
            self.casillas2[k].grid(row = k + 2, column = 2, sticky = 'ew')
            k += 1
        
        #imprimir cuenta
        self.lblCuenta = Label(self.root, font  = ("Times", "15", "italic"))
        self.lblCuenta.pack()
    
    def nuevaOrden(self):
        self.nombre.delete(0, END)
        self.costo = 0
        self.orden = []
        self.lblCuenta['text'] = ''
    
    def cuenta(self, key, e):
        if key == 'a':
            self.orden.append(self.Lplatillo[e][0])
            self.costo += self.Lplatillo[e][1]
            
        elif key == 'b':
            self.orden.append(self.Lbebida[e - len(self.Lplatillo)][0])
            self.costo += self.Lbebida[e - len(self.Lplatillo)][1]
        
        self.lblCuenta['text'] = "Orden de " + self.nombre.get() + ": " + str(self.orden) + "  $" + str(self.costo)                                                                        

root = Tk()
miMenu = interfazMenu(root)
root.mainloop()