# print("Ejercicio 1")
# print(" ¡Hola Mundo!")
# 
# print("Ejercicio 2")
# var = "¡Hola Mundo!"
# print(var)
# 
# print("Ejercicio 3")
# nombre = input("Dime tu nombre: ")
# print("¡Hola " + nombre + " !")
from html.parser import interesting_normal

# print("Ejercicio 4")
# nombre = input("Dime tu nombre: ")
# n = input("Dime un número: ")
# print((nombre + "\n") * int(n))

# print("Ejercicio 5")
# nombre = input("Dime tu nombre: ")
# print(nombre + " tiene " + str(len(nombre)) + " letras")

# print("Ejercicio 6")
# a = ((3+2)/(2*5))**2
# print(a)
# 
# print("Ejercicio 7")
# horas = float(input("¿Horas trabajadas?"))
# coste = float(input("¿Coste por hora?"))
# paga = horas * coste
# print("Tu paga es : " + str(paga))

# print("Ejercicio 8")
# n = int(input("Introduce un nº: "))
# suma = int(n*(n+1)/2)
# print(suma)

# print("Ejercicio 9")
# peso = float(input("Introduce tu peso en Kg: "))
# altura= float(input("Introduce tu altura en m: "))
# masa_corporal = peso / altura**2
# print("Tu índice de masa corporal es: " + str(masa_corporal))

# print("Ejercicio 10")
# n = int(input("Introduce un nº: "))
# m = int(input("Introduce un nº: "))
# c = n / m
# r = n % m
# print(str(n) + " entre " + str(m) + " da un cociente de " + str(c) + " y un resto de " + str(r))    

# print("Ejercicio 11")
# invertir = float(input("Cuanto vas a invertir? "))
# interes = float(input("Interés anual = "))
# anio = int(input("Nº de años? "))
# capital_total = invertir * (1 + interes/100) **anio
# print(capital_total)

# print("Ejercicio 12")
# peso_payaso = 112
# peso_muneca = 75
# payasos = int(input("Cuantos Payasos? "))
# munecas = int(input("Cuantas Muñecas? "))
# print("Payasos vendidos= " + str(payasos) + "\nMuñecas vendidas= " + str(munecas) +
#       "\nTotal venta = " + str(payasos + munecas))
# print("Total peso: " + str((payasos * peso_payaso) + (munecas * peso_muneca)))

# print("Ejercicio 13")
# dinero = float(input("Dinero depositado:"))
# interes = 0.04
# anioUno = round(dinero + (dinero * interes),2)
# anioDos = round(anioUno + (anioUno * interes),2)
# anioTres = round(anioDos + (anioDos * interes),2)
# print("Ahorros 1º año= " + str(anioUno) + "\nAhorros 2º año= " + str(anioDos) +
#       "\nAhorros 3º año= " + str(anioTres))

print("Ejercicio 14")
pan = 3.49
descuento = 0.6
pan_duro = 3.49 - (3.49*0.6)
pan_vendido= int(input("Nº pan duro "))
print("Precio Pan: " + str(pan) + "\nDescuento: 60%" + "\nTotal: " + str(round(pan_vendido * pan_duro ,2)))




