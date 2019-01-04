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

        button1=Button(self.root,text='Izquierda', command = lambda: self.mover('a'))
        button2=Button(self.root,text='Derecha', command = lambda: self.mover('b'))
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
            
        self.juegoPerdido()
        self.root.after(50, self.muros)
        
    def mover(self, k):
        self.k = k
        self.x1,self.y1,self.x2,self.y2 = self.lienzo.coords(self.posicion)
    
        if self.k == 'a':
            self.lienzo.coords(self.posicion, self.x1-100, self.y1, self.x2-100, self.y2)

        if self.k == 'b':
            self.lienzo.coords(self.posicion, self.x1+100, self.y1, self.x2+100, self.y2)
            
        self.juegoPerdido()
    
    def juegoPerdido(self):
        if  self.d >= self.y1 and self.k =='a':
            print('Chocaste izquierda')

        if self.d2 > self.y1 and (self.k =='b' or self.k == ''):
            print('Chocaste derecha')

              
    

root=Tk()
juego = juegoCoche(root)
root.mainloop()