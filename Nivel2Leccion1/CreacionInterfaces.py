from tkinter import *

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.crearWidgets()
        self.master.geometry("600x300+5+40")
        #root.lift()#lower()
        #root.after(2000, self.master.quit)
        
    def crearWidgets(self):
        self.etiqueta = Label(self.master, cursor = "pencil", fg = "red", bg = "white",
                 text = """Texto de la etiqueta. Si ocupa varios renglones,
poner doble comilla triple al escribir la cadena""",
                 font  = ("Times", "12", "italic"))
        self.etiqueta.pack(side = 'left')
        
        self.boton = Button(self.master, text = "Cerrar ventana", command = self.master.quit)
        self.boton.pack(side = 'bottom', padx = '20', ipady = '25')
        
        self.etiqueta2 = Label(self.master, text = 'Hola Mundo', cursor = 'pencil')
        self.etiqueta2.pack()

#Creación de la ventana raíz de la GUI
root = Tk()

#root.minsize(300, 300)
#root.maxsize(900, 900)
#root.geometry("900x300")
#root.title("Mi Primera Interfaz")
root.title("Hola")

gui = Interfaz(root)
root.mainloop()


#cursores: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html