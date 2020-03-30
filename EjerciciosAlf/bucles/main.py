#http://aprendeconalf.es/python/ejercicios/bucles.html
import bucles.funciones

print('''1.Pide al usuario una palabra y la muestre 10 veces
2.Pide la edad y muestra todos los años que ha cumplido (desde 1 hasta su edad)
3.Pide un nº entero positivo y muestre todos los números impares desde 1 hasta ese número separados por comas.
4.Pide un nº entero positivo y muestre cuenta atrás desde ese número hasta cero separados por comas.
5.Pide una cantidad a invertir, el interés anual y el número de años, y muestre
    el capital obtenido en la inversión cada año que dura la inversión.
6.Pide un nº entero y muestre un triángulo rectángulo de altura el número introducido
7.Un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
8.Pide al usuario un nº entero y muestre un triángulo rectángulo de altura el nº introducido impares
9.Almacenar la cadena de caracteres contraseña en una variable, pregunte al usuario 
    por la contraseña hasta que introduzca la contraseña correcta.
10.Pide al usuario un número entero y muestre por pantalla si es un número primo o no.
11.Pide al usuario una palabra y luego muestre una a una las letras de la palabra 
    introducida empezando por la última.
12.Pide al usuario por una frase y una letra, y muestre el número de veces que aparece
    la letra en la frase.
13.Muestra el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
''')
a = int(input("¿Qué ejercicio quieres ver? "))

if a == 1:
    bucles.funciones.ejercicio1()
elif a == 2:
    bucles.funciones.ejercicio2()
elif a == 3:
    bucles.funciones.ejercicio3()
elif a == 4:
    bucles.funciones.ejercicio4()
elif a == 5:
    bucles.funciones.ejercicio5()
elif a == 6:
    bucles.funciones.ejercicio6()
elif a == 7:
    bucles.funciones.ejercicio7()
elif a == 8:
    bucles.funciones.ejercicio8()
elif a == 9:
    bucles.funciones.ejercicio9()
elif a == 10:
    bucles.funciones.ejercicio10()
elif a == 11:
    bucles.funciones.ejercicio11()
elif a == 12:
    bucles.funciones.ejercicio12()
elif a == 13:
    bucles.funciones.ejercicio13()   
    
    
