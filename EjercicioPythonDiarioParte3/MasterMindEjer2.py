'''
Adivinar una cadena de números distintos. Al principio, pedir la longitud de la cadena (de 2 a 9 cifras). 
Después debe ir pidiendo que intentes adivinar la cadena de números. En cada intento, el programa 
informará de cuántos números han sido acertados (el programa considerará que se ha acertado 
un número si coincide el valor y la posición).
'''
import random

size = int(input("Introduce la longitud de la cadena de 2 a 9 cifras: "))
valores = ["0","1","2","3","4","5","6","7","8","9"]
number= random.sample(valores, size)        #nº aleatorio entre los valores y longitud dada

# text = "".join(number)        #para resolver con trampas!! 
# print(text)   
        
acertar = False
while acertar == False:
    a = input("Intenta adivinar la cadena: ")
    option = list(a)
    n = 0
    i = 0
    for indice in number:
        if indice == option[i]:
            n +=1
            i +=1
        else:
            i +=1
    if n < size:
        print("Has acertado " + str(n) + " valores")
    if n == size:
        print("Muy bien! Eres un fiera!")
        acertar = True
              
       


