from tkinter import *


window = Tk()

def km_to_miles():
    
    miles=float(e1_value.get())*1.6
    #Agrega a la "caja" text lo que tiene miles, donde el END indica que se agrega al final de lo que tiene la "caja"
    t1.insert(END, miles)

#Crea el Boton, lo agrega a la ventana y le pone el testo de "Execute", y le agrega el comando a ejecutar
b1=Button(window, text="Execute", command=km_to_miles)
#Posicion del boton en la ventana
b1.grid(row = 0, column = 0)

e1_value = StringVar()
e1= Entry(window, textvariable=e1_value)
e1.grid(row = 0, column = 1)
#Crea el campo de texto, lo asigna a window y le da tamaño con height and width
t1 =  Text(window, height=1, width=20)
#Asigna la posicion en la ventana
t1.grid(row = 0, column = 2)

#es para mantener la ventana abierta y va despúes del codigo a ejecutar
window.mainloop()