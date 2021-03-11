#script que pasa de KG a gramos, libras y onzas
from tkinter import *

window = Tk()
#cambiando titulo de la ventana
window.title("Convert KG to...")

#La función que va a hacer el boton
def conversion():
    #Cambia el tipo de dato de la entrada a float y la multiplica para sacar gramos
    grams= float(e1_entrada.get())*1000
    #Cambia el tipo de dato de la entrada a float y la multiplica para sacar libras
    pounds= float(e1_entrada.get())*2.20462
    #Cambia el tipo de dato de la entrada a float y la multiplica para sacar onzas
    ounces= float(e1_entrada.get())*35.274
    
    #elimina lo que tenga la caja de texto
    tgrams.delete("1.0", END) 
    #Agrega el valor de la variable a a caja de texto
    tgrams.insert(END, grams)
    tpounds.delete("1.0", END) 
    tpounds.insert(END, pounds)
    tounces.delete("1.0", END) 
    tounces.insert(END, ounces)
    
    

label = Label(window, text = "KG" )
label.grid(row = 0, column = 0)

e1_entrada= StringVar()
e1=Entry(window, textvariable=e1_entrada )
e1.grid(row = 0, column =1)

b1=Button(window, text = 'Convert ', command = conversion)
b1.grid(row=0, column = 2)

labelg = Label(window, text = "Grams" )
labelg.grid(row = 1, column = 0)

labelp = Label(window, text = "Pounds" )
labelp.grid(row = 1, column = 1)

labelo = Label(window, text = "Ounces" )
labelo.grid(row = 1, column = 2)


tgrams= Text(window, height=1, width=20)
tgrams.grid(row = 2, column =0)

tpounds=Text(window, height=1, width=20)
tpounds.grid(row = 2, column =1)

tounces=Text(window, height=1, width=20)
tounces.grid(row = 2, column =2)

window.mainloop()