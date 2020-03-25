'''Ejercicio 3 
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las 
tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas 
tiene que decir que riman un poco y si no, que no riman.
'''

def rimarPalabras():
    cont = "s"
    while cont != "n":
        wordOne = input("Dime una palabra ")
        wordTwo = input("Dime otra palabra ")
        if len(wordOne) >= 3 and len(wordTwo) >= 3:
            if wordOne[-3:] == wordTwo[-3:]:
                print("Las palabras " + wordOne + " y " + wordTwo + " si riman")
                cont = input("¿Seguimmos?  S/N ").lower()
               
            elif wordOne[-2:] == wordTwo[-2:]:
                print("Las palabras " + wordOne + " y " + wordTwo + " riman un poco")
                cont = input("¿Seguimmos?  S/N ").lower()
            else:
                print("Las palabras " + wordOne + " y " + wordTwo + " no riman")
                cont = input("¿Seguimmos?  S/N ").lower()
        else:
            print("Las palabras tienen que tener al menos 3 letras!")
    print("Fin del Juego")

#rimarPalabras()