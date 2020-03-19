from tkinter import *
from tkinter import messagebox
from datetime import datetime

x = 0
y = 0
resuelta = 5
imagenes = [False, False, False, False, False]

def hacer_clic(evento):
    global x, y
    x = evento.x
    y = evento.y  
    if x >= 644 and x <=684 and y >= 65 and y <= 85:
        comprobar_acierto(0)        
    elif x >= 998 and x <=1030 and y >= 109 and y <= 131:
        comprobar_acierto(1) 
    elif x >= 832 and x <=879 and y >= 169 and y <= 202:
        comprobar_acierto(2) 
    elif x >= 584 and x <=622 and y >= 219 and y <= 242:
        comprobar_acierto(3) 
    elif x >= 738 and x <=782 and y >= 305 and y <= 330:
        comprobar_acierto(4) 
    else:
        if resuelta == 5:
            messagebox.showerror("No, no..", "Eso no es diferente.\nNo has encontrado ninguna diferencia")
        else: 
            messagebox.showerror("No, no..", "Eso no es diferente.\nTe quedan " + str(resuelta) + " diferencias")
#end hacer_click

def comprobar_acierto(index):
    if imagenes[index] == False:
        aciertos()
        imagenes[index] = True
    else:
        messagebox.showerror("Repetida", "Esa imagen ya la habías encontrado")   
#end comprobar_aciertos
    
def aciertos():
    global resuelta
    resuelta -=1
    if resuelta != 0:
        messagebox.showinfo("Bien", "Has encontrado una diferencia!! \n >>> Te quedan: " + str(resuelta))
    else:
        time_fin = datetime.now()
        tiempoTotal2 = time_fin - time_ini
        messagebox.showinfo("Felicidades!", "Has encontrado todas las diferencias")
        messagebox.showinfo("Tiempo", "Inicio Juego: " + str(time_ini.strftime("%H:%M:%S")) +
                            "\nFin Juego: " + str(time_ini.strftime("%H:%M:%S")) +
                            "\nTiempo en resolver: "+ str(tiempoTotal2))
        datos = open("users.txt", "a")
        datos.write("\n>>>>Tiempo: " + str(tiempoTotal2))
        datos.close()
        ventana.destroy()        
#end aciertos

def input_value():
    nombre = value_label.get()  # Obtenemos el número de la StringVar
    datos = open("users.txt", "a")
    datos.write("\n\nNombre Usuario: " + nombre)
    datos.close()
    usuario.destroy()
#end input_value

ventana = Tk()

#creamos canvas para posicionar la imagen en la ventana
canvas = Canvas(ventana,width = 800, height = 600)
canvas.pack(expand = YES, fill = BOTH)
imagen = PhotoImage(file= "imagen2.png")   
canvas.create_image(32,40, image = imagen, anchor = NW) 

#damos valores a la ventana que se va a crear
ventana.geometry("1100x400")
ventana.title("Diferencias")
ventana.bind("<Button 1>", hacer_clic)

value_label = StringVar()
#ventana donde solicita nombre de usuario
usuario = Toplevel(ventana)
usuario.title("Usuario")
usuario.geometry("370x150+580+360")
usuario.attributes("-topmost", True)
Label(usuario, text="Nombre de Usuario:").place(x=5, y=20)
Entry(usuario, width = 50, textvariable=value_label).place(x=5, y=50)
Button(usuario, text="Aceptar", command = input_value).place(x=120, y=90)


#muestro archivo con los datos de usuarios y tiempos
datos_usuario = open("users.txt", "r")
datos = datos_usuario.read()
print(datos)
datos_usuario.close()

messagebox.showinfo("Juego de Diferencias", 
                    "ENCUENTRA LAS 5 DIFERENCIAS EN LA IMAGEN DE LA DERECHA.\n HAZ CLICK EN ELLAS.")

time_ini = datetime.now() #tiempo de comienzo desde el cierre de la ventana de inicio juego

ventana.mainloop()



