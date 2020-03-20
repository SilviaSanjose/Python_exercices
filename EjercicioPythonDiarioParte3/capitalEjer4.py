'''Ejercicio 4
Pide al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos 
esos años si cada año se aplica la tasa de interés introducida.
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés 
anual se convierte en 24117.14 dolares al cabo de 20 años.'''

dollar = int(input("Introduce los dólares "))
tax = float(input("Introduce tasa de interés "))
year = int(input("Introduce los años "))

capital = round(dollar * (1 + tax/100)** year,2)
print("Tu capital en " + str(year) + " será de " + str(capital) + "€")