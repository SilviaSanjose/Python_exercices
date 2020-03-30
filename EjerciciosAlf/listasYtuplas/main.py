#http://aprendeconalf.es/python/ejercicios/listas-tuplas.html
import listasYtuplas.funciones

print('''1.Almacena las asignaturas de un curso en una lista y la muestre por pantalla.
2.Almacena las asignaturas de un curso en una lista y muestre una a una "Yo estudio 'asignatura'"
3.Almacena las asignaturas en una lista, pregunta al usuario la nota que ha sacado en 
    cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
    has sacado <nota>
4.Pregunta los nº ganadores de la lotería, los almacene en lista y los muestre ordenados de menor a mayor.
5.Almacena en lista los nº del 1 al 10 y los muestre en orden inverso separados por comas.
6.Almacena las asignaturas en una lista, pregunta al usuario la nota que ha sacado en cada asignatura 
    y elimine de la lista las asignaturas aprobadas. Y mostrar las asignaturas suspendidas
7.Almacena el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos 
    de 3, y muestre por pantalla la lista resultante.
8.Pide al usuario una palabra y muestre por pantalla si es un palíndromo (como capicúa pero en letras)
9.Pide al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
10.Almacena en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestra el menor y 
    el mayor de los precios.
11.Almacena los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
12.PENDIENTE:Almacenar dos matrices en una lista y mostrar su producto.
13.PENDIENTE:
''')
a = int(input("¿Qué ejercicio quieres ver? "))

if a == 1:
    listasYtuplas.funciones.ejercicio1()
elif a == 2:
    listasYtuplas.funciones.ejercicio2()
elif a == 3:
    listasYtuplas.funciones.ejercicio3()
elif a == 4:
    listasYtuplas.funciones.ejercicio4()
elif a == 5:
    listasYtuplas.funciones.ejercicio5()
elif a == 6:
    listasYtuplas.funciones.ejercicio6()
elif a == 7:
    listasYtuplas.funciones.ejercicio7()
elif a == 8:
    listasYtuplas.funciones.ejercicio8()
elif a == 9:
    listasYtuplas.funciones.ejercicio9()
elif a == 10:
    listasYtuplas.funciones.ejercicio10()
elif a == 11:
    listasYtuplas.funciones.ejercicio11()
elif a == 12:
    listasYtuplas.funciones.ejercicio12()
elif a == 13:
    listasYtuplas.funciones.ejercicio13()   
    

