from tkinter import *

class App:
    def __init__(self, root):
        self.root = root
        self.Principal()
        
    def Principal(self):
        #variables de control
        self.Decimal = DoubleVar()
        self.Cadena = StringVar()
        
        #manipulación
        #self.Decimal.set(7.0)
        self.Cadena.set(' ')
        self.Decimal.trace('w', self.Cambio)
        
        #widgets
        self.entrada = Entry(self.root, textvariable = self.Decimal)
        self.radio1 = Radiobutton(self.root, text = 'Redondear', variable = self.Cadena, value = 'a', command = self.Redondear)
        self.radio2 = Radiobutton(self.root, text = 'Truncar', variable = self.Cadena, value = 'b', command = self.Truncar)
        
        #empaquetar
        self.entrada.pack()
        self.radio1.pack()
        self.radio2.pack()
        
    def Redondear(self):
        self.numRed = round(self.Decimal.get(), 2)
        print('Entrada redondeada: ', self.numRed)
    
    def Truncar(self):
        self.numRed = int(self.Decimal.get())
        print('Entrada truncada: ', self.numRed)
    
    def Cambio(self, *args):
        print('La entrada cambió a: ', self.Decimal.get())
        
root = Tk()
iniciar = App(root)
root.mainloop()