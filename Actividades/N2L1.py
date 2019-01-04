from tkinter import *

class interfazMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido al restaurante")
        self.root.minsize(400, 300)
        self.Lplatillo = [["pollo", 20], ["pescado", 30]]
        self.Lbebida = [["agua", 5], ["jugo", 10], ["refresco", 10]]
        self.imprimirMenu()
    
    def imprimirMenu(self):     
        #Nombre cliente
        self.lblCliente = Label(self.root, text = "Cliente", font  = ("Times", "15", "italic"))
        self.lblCliente.pack()
        self.nombre = Entry(self.root)
        self.nombre.pack()
        
        #Concepto y costo
        self.lblConcepto = Label(self.root, text = "Concepto", font  = ("Times", "15", "italic"))
        self.lblConcepto.pack()
        self.lblCosto = Label(self.root, text = "Costo", font  = ("Times", "15", "italic"))
        self.lblCosto.pack()
        
        #Platillo
        self.lblPlatillo = Label(self.root, text = "Platillo", font  = ("Times", "15", "italic"))
        self.lblPlatillo.pack()
        
        #Bebida
        self.lblBebida = Label(self.root, text = "Bebida", font  = ("Times", "15", "italic"))
        self.lblBebida.pack()
        
root = Tk()
miMenu = interfazMenu(root)
root.mainloop()