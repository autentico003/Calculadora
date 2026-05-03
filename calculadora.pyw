from tkinter import *


raiz = Tk()

raiz.title("Calculadora")

raiz.geometry("260x470")
raiz.resizable(1,1)
raiz.config(bg="light gray")





framePantalla=Frame()
framePantalla.config(bg="blue")
framePantalla.grid(row=0)



"""frameCientifica=Frame()
frameCientifica.config(bg="black")
frameMoneda=Frame()


barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)
archivoMenu=Menu(barraMenu, tearoff=0, fg="black", font=("Cambria", 10))

barraMenu.add_cascade(label="Mas", menu=archivoMenu)
archivoMenu.add_command(label="Estandar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cientifica")
archivoMenu.add_separator()
archivoMenu.add_command(label="Moneda")"""





i=0
def enviar(dato):
    global i
    i +=1
    pantalla.insert(i, dato)


def operacion():
    global i
    ecuacion = pantalla.get()
    if i != 0:
        try:
            result = str(eval(ecuacion))
            pantalla.delete(0, END)
            pantalla.insert(0, result)
            longitud = len(result)
            i = longitud

        except:
            result = "ERROR"
            pantalla.delete(0, END)
            pantalla.insert(0, result)

    else:
        pass


def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		pantalla.delete(i,last =None)
		i-=1


def borrar_todo():
    pantalla.delete(0, END)
    i=0




pantalla= Entry(raiz, width=28, bg="white", bd=6, font=("cambria",10, "bold"),
fg="black",relief="sunken",cursor="hand2")
pantalla.grid(row=0, padx=6, pady=20,columnspan=4, ipady=15)

boton_frameEstandar = Button(raiz, text="√", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar('**(1/2)')).grid(row=1, column=0,padx=2, pady=2)

boton_comenzar = Button(raiz, text="C", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command=borrar_todo).grid(row=1, column=1,padx=2, pady=2)

boton_pi = Button(raiz, text="pi", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar('*3,141516')).grid(row=1, column=2,padx=2, pady=2)

boton_dividir = Button(raiz, text="/", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar('/')).grid(row=1, column=3,padx=2, pady=2)

boton7 = Button(raiz, text="7", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda: enviar(7)).grid(row=2, column=0,padx=2, pady=2)

boton8 = Button(raiz, text="8", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(8)).grid(row=2, column=1,padx=2, pady=2)

boton9 = Button(raiz, text="9", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(9)).grid(row=2, column=2,padx=2, pady=2)

boton_multiplicar= Button(raiz, text="x", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar('*')).grid(row=2, column=3,padx=2, pady=2)

boton4 = Button(raiz, text="4", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(4)).grid(row=3, column=0,padx=2, pady=2)

boton5 = Button(raiz, text="5", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command=lambda : enviar(5)).grid(row=3, column=1,padx=2, pady=2)

boton6 = Button(raiz, text="6", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(6)).grid(row=3, column=2,padx=2, pady=2)

boton_resta= Button(raiz, text="-", font=("cambria", 14, "bold"), fg="black", justify="center", bg="gray", 
                height=2, width=4,cursor="hand2", command= lambda : enviar('-')).grid(row=3, column=3,padx=2, pady=2)

boton1 = Button(raiz, text="1", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(1)).grid(row=4, column=0,padx=2, pady=2)

boton2 = Button(raiz, text="2", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(2)).grid(row=4, column=1,padx=2, pady=2)

boton3 = Button(raiz, text="3", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(3)).grid(row=4, column=2,padx=2, pady=2)

boton_suma= Button(raiz, text="+", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar('+')).grid(row=4, column=3,padx=2, pady=2)

boton0 = Button(raiz, text="0", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(0)).grid(row=5, column=0,padx=2, pady=2)

boton_coma = Button(raiz, text=",", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= lambda : enviar(',')).grid(row=5, column=1,padx=2, pady=2)

boton_borrar= Button(raiz, text="Del", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command= borrar_uno).grid(row=5, column=2,padx=2, pady=2)

boton_bigual= Button(raiz, text="=", font=("cambria", 14, "bold"), fg="black", bg="gray", 
                height=2, width=4, justify="center",cursor="hand2", command=operacion).grid(row=5, column=3,padx=2, pady=2)

icono=PhotoImage(file="CalculadoraFondo.png")
Label(raiz, image=icono).grid(row=6, columnspan=4)
raiz.mainloop()

