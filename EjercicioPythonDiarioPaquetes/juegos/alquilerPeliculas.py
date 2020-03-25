'''
Muestra primero el listado de categorías de películas y pide al usuario que introduzca
el código de la categoría de la película y posterior a ello pide que el usuario 
introduzca el número de días de atraso, y así se muestra al final el total a pagar.
'''
def alquilarpelis():

    def pagar():
        if code_int == 1:
            pay = 2.50 + (days * 0.50)
        elif code_int == 2:
            pay = 3.00 + (days * 0.75)
        elif code_int == 3:
            pay = 3.50 + (days * 1.00)    
        elif code_int == 4:
            pay = 4.00 + (days * 1.50)   
        print("Tienes que pagar " + str(pay) + "€")
    #end pagar
    
    print('''      CATEGORIA       PRECIO     CODIGO    RECARGO/DIA DE ATRASO
        Favoritos          2.50€        1          0.50€
        Nuevos             3.00€        2          0.75€
        Estrenos           3.50€        3          1.00€
        Super Estrenos     4.00€        4          1.50€''')
    print('')
    
    code_num= False
    while code_num == False:
        code = input("Introduzca el código de la película: ")
        try:
            code_int = int(code)
            if code_int > 4:
                print("Ese no es un código válido")
            else:
                days = int(input("Introduzca el número de dias de retraso en devolución: "))
                pagar()
                codeNew = input("¿Quieres devilver otra película? S/N ").lower()
                if codeNew == "n":
                    print("Hasta luego!")
                    code_num = True
        except:
            print("Eso no es un número de código")
    
