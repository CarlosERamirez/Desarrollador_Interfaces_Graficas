from tkinter import *

class Dibujar:
    def __init__(self, root):
        self.root = root
        self.root.title('Caballete')
        self.Principal()
        
    def Principal(self):   
        lienzo = Canvas(self.root, width = 400, height = 150, bg = 'white')
        lienzo.pack()
        
        posicion = lienzo.create_line(50, 100, 350, 100, fill="red")
        lienzo.create_rectangle(0, 25, 50, 75, fill="blue")
        lienzo.create_polygon(120, 50, 50, 75, 350, 75, fill = 'yellow')
        lienzo.create_text(100, 50, text = "Mi Lienzo")
        
        xy = 300, 0, 350, 100
        lienzo.create_arc(xy, start=0, extent=230, fill="blue")
        lienzo.create_arc(xy, start=230, extent=90, fill="green")
        
        x1, y1, x2, y2 = lienzo.coords(posicion)
        lienzo.coords(posicion, x1 + 5, y1 + 5, x2 + 15, y2 + 15)
                 
root = Tk()
gui = Dibujar(root)
root.mainloop()