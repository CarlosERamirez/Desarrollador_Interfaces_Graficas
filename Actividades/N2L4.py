"""from tkinter import *

class Estrella:
    def __init__(self, root):
        self.root = root
        self.Principal()
        self.mover()
        
    def Principal(self):   
        self.lienzo = Canvas(self.root, width = 400, height = 400, bg = 'white')
        self.lienzo.pack()
        
        self.posicion = self.lienzo.create_polygon(200, 50, 237.5, 162.5, 350, 200, 237.5, 237.5, 200,
                              350, 162.5, 237.5, 50, 200, 162.5, 162.5, fill = "yellow")
        
    def mover(self):
        Dx=1
        Dy=1
        a,a2,b,b2,c,c2,d,d2,e,e2,f,f2,g,g2,h,h2=self.lienzo.coords(self.posicion)        
        
        self.lienzo.coords(self.posicion,
                           a-Dx,a2-Dy,b-Dx,b2-Dy,
                           c-Dx,c2-Dy,d-Dx,d2-Dy,
                           e-Dx,e2-Dy,f-Dx,f2-Dy,
                           g-Dx,g2-Dy,h-Dx,h2-Dy)

        root.after(10,self.mover)

root = Tk()
gui = Estrella(root)
root.mainloop()"""


from tkinter import *  

class juegoCoche:
    def __init__(self, root):
        self.root = root
        self.x1,self.y1,self.x2,self.y2 = 0, 0, 0, 0
        self.d, self.d2 = 0, 0
        self.k = ''
        self.widgets()
        self.muros()
    
    def widgets(self):    
        self.lienzo = Canvas(self.root, width=200, height=500, bg='white')
        self.lienzo.pack()

        button1=Button(self.root,text='Izquierda')
        button2=Button(self.root,text='Derecha')
        button1.pack(side = "left")
        button2.pack(side = "right")

        velocidad = Button(self.root, text = 'velocidad', command = self.muros)
        velocidad.pack()

        self.muro1 = self.lienzo.create_rectangle(0, 0, 100, 20, fill = 'black')
        self.muro2 = self.lienzo.create_rectangle(100, 160, 200, 180, fill = 'black')

        self.posicion = self.lienzo.create_rectangle(120, 410, 180, 490, fill = 'black')
    
    def muros(self):
        a,b,c,self.d = self.lienzo.coords(self.muro1)
        a2,b2,c2,self.d2 = self.lienzo.coords(self.muro2)
    
        self.lienzo.coords(self.muro1, a,b + 5,c,self.d + 5)
        self.lienzo.coords(self.muro2, a2,b2 + 5,c2,self.d2 + 5)
        if self.d >= 500:
            a,b,c,self.d = 0, 0, 100, 20
            a2,b2,c2,self.d2 = 100, 160, 200, 180
            self.lienzo.coords(self.muro1, a,b + 5,c,self.d + 5)
            self.lienzo.coords(self.muro2, a2,b2 + 5,c2,self.d2 + 5)
        
        self.x1,self.y1,self.x2,self.y2 = self.lienzo.coords(self.posicion)
        self.root.after(50, self.muros)


root=Tk()
juego = juegoCoche(root)
root.mainloop()