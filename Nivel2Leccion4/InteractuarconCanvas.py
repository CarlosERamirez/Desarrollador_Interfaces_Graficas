from tkinter import *

class Dibujar:
    def __init__(self, root):
        self.root = root
        self.root.title('Caballete')
        self.Principal()
        
    def Principal(self):
        self.lienzo = Canvas(self.root, width = 400, height = 400, bg = 'white')
        self.lienzo.pack()
        
        boton = Button(self.root, text = 'Dibujar', command = self.Dibujo)
        self.lienzo.create_window(200, 10, window = boton)
    
    def Dibujo(self):        
        self.lienzo.bind("<B1-Motion>",
                    lambda e: self.lienzo.create_oval(e.x - 2,
                                                 e.y - 2,
                                                 e.x + 2,
                                                 e.y + 2,
                                                 fill = 'black'))
        
root = Tk()
gui = Dibujar(root)
root.mainloop()