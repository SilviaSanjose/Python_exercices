from diccionarios import funciones

print('''1.Crea diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
        y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
2.Pregunte al usuario su nombre, edad, dirección y teléfono y guardar en un diccionario. Después debe mostrar 
       por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
3.Guarde en un diccionario precios de frutas, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
       el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
4.Pregunta una fecha en formato dd/mm/aaaa y muestre la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

5.Diccionario con asignaturas y créditos, y muestre "La asignatura <nombre> tiene <créditos> creditos y al final, la suma de créditos
    
6.Crear un diccionario vacío y lo llene con información que se pide al usuario.

7.Crear diccionario que simule una cesta de la compra.Preguntar articulos y precio, y añadirlos al diccionario. Después mostrar la lista

8.Crear diccionario, preguntando al usuario las palabras a incluir en formato "español:ingles". Después preguntar una frase, si las palabras están 
      en el diccionario, traducirla, y si no, dejarla en español

9.Crear diccionario preguntando al usuario por nº de factura(clave) y coste(valor). Preguntar si quiere añadir factura, pagar factura existente:
      Si paga,eliminar la factura del diccionario. Mostrar tras cada operación la cantidad cobrada y pendiente de cobro.
    
10.Programa que gestione la base de datos de unos clientes. Los clientes se guardan en un diccionario, donde cada cliente es una clave(dni), y el valor
       otro diccionario con los datos; nombre, direccion, telefono, correo, preferente (True o False). Preguntar varias operaciones a realizar.
''')

option = True

while option == True:
    a = int(input("¿Qué ejercicio quieres ver? "))
    if a == 1:
        funciones.ejercicio1()
    elif a == 2:
        funciones.ejercicio2()
    elif a == 3:
        funciones.ejercicio3()
    elif a == 4:
        funciones.ejercicio4()
    elif a == 5:
        funciones.ejercicio5()
    elif a == 6:
        funciones.ejercicio6()
    elif a == 7:
        funciones.ejercicio7()
    elif a == 8:
        funciones.ejercicio8()
    elif a == 9:
        funciones.ejercicio9()
    elif a == 10:
        funciones.ejercicio10()
    continuar = input("¿Quieres ver otro ejercicio? S/N : ").lower()
    if continuar == "n":
        option = False
        print("Fin")