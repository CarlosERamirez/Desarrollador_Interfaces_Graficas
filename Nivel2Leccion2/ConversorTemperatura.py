from tkinter import *

class ConversorTemperatura:
    def __init__(self, root):
        self.root = root
        self.root.title('Conversor de Temperaturas')
        #self.root.geometry('320x150')
        self.Inicializar()
        
    def Inicializar(self):
        #variables de control
        self.varGrados = DoubleVar()
        self.varGrados2 = DoubleVar()
        self.escala = StringVar()
        self.escala.set('c')
        self.escala2 = StringVar()
        self.escala2.set('c')
        
        #marcos
        self.marco1 = Frame(self.root)
        self.marco2 = Frame(self.root)
        
        #widgets
        self.entrada1 = Entry(self.marco1, textvariable = self.varGrados)
        self.radio1 = Radiobutton(self.marco1,
                                  text = 'Celsius',
                                  variable = self.escala,
                                  value = 'c',
                                  command = lambda: self.Convertir(1))
        self.radio2 = Radiobutton(self.marco1,
                                  text = 'Fahrenheit',
                                  variable = self.escala,
                                  value = 'f',
                                  command = lambda: self.Convertir(1))
        self.radio3 = Radiobutton(self.marco1,
                                  text = 'Kelvin',
                                  variable = self.escala,
                                  value = 'k',
                                  command = lambda: self.Convertir(1))
        
        self.entrada2 = Entry(self.marco2, textvariable = self.varGrados2)
        self.radio4 = Radiobutton(self.marco2, text = 'Celsius',
                                  variable = self.escala2,
                                  value = 'c',
                                  command = lambda: self.Convertir(0))
        self.radio5 = Radiobutton(self.marco2, text = 'Fahrenheit',
                                  variable = self.escala2,
                                  value = 'f',
                                  command = lambda: self.Convertir(0))
        self.radio6 = Radiobutton(self.marco2,
                                  text = 'Kelvin',
                                  variable = self.escala2,
                                  value = 'k',
                                  command = lambda: self.Convertir(0))
          
        #empaquetar
        self.marco1.pack(side = 'left')
        self.marco2.pack(side = 'right')
        
        self.entrada1.pack()
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
        
        self.entrada2.pack()
        self.radio4.pack()
        self.radio5.pack()
        self.radio6.pack()
            
    def Convertir(self, key):
        self.key = key
        
        if self.key == 0:
            self.var = self.varGrados.get()
            self.tupEscalas = (self.escala.get(), self.escala2.get())
            self.configurar = self.varGrados2
 
        elif self.key == 1:
            self.var = self.varGrados2.get()
            self.tupEscalas = (self.escala2.get(), self.escala.get())
            self.configurar = self.varGrados
   
        self.diccFormulas = {('f', 'c'): 5*(self.var-32)/9,
                            ('k', 'c'): self.var - 273.15,
                            ('c', 'f'): 9*self.var/5 + 32,
                            ('k', 'f'): 9*(self.var - 273.15)/5 + 32,
                            ('c', 'k'): self.var + 273.15,
                            ('f', 'k'): 5*(self.var-32)/9 + 273.15,
                            ('c', 'c'): self.var,
                            ('f', 'f'): self.var,
                            ('k', 'k'): self.var,
                            }
        
        self.configurar.set(round(self.diccFormulas[self.tupEscalas], 2))  

root = Tk()
iniciar = ConversorTemperatura(root)
root.mainloop()