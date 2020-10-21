#http://aprendeconalf.es/python/ejercicios/listas-tuplas.html


def ejercicio1():
    asig = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    print(asig)

def ejercicio2():
    asig = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    for i in asig:
        print("Yo estudio " + i)

def ejercicio3():
    asig = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    notas = []
    for i in asig:
        nota = float(input("Que nota has sacado en " + i + " "))
        notas.append(i + " tienes de nota "+ str(nota))
    for n in notas:
        print(n)

def ejercicio4():
    number = input("Indica lo números ganadores de la lotería: ")
    numbers = number.split()
    numbers.sort()
    print(numbers)

def ejercicio5():
    numbers =[]
    for i in range(1,11):
        numbers.append(i)
    numbers.reverse()
    for n in numbers:
        print(n, end = "-")

def ejercicio6():
    asig = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    asig_sus = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    for i in asig:
        nota = float(input("Que nota has sacado en " + i + " "))
        if nota >= 5:
            asig_sus.remove(i)
    print(asig_sus)

def ejercicio7():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    multi = []
    for i in range(1, len(abc)):
        if i % 3 == 0:
            multi.append(abc[i])
    for i in multi:
        abc.remove(i)
    print(abc)
       
def ejercicio8():
    word = input("Introduce una palabra: ")
    word_list = list(word)
    word_list_rev = list(word)
    word_list_rev.reverse()
    if word_list == word_list_rev:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
 
def ejercicio9():
    word = input("Introduce una palabra: ")
    letter = ['a', 'e','i','o','u']
    for l in letter:
        count = 0
        for w in word:
            if l == w:
                count +=1
        print("La letra " + l + " aparece " + str(count) + " veces")
    
def ejercicio10():
    price = [50, 75, 46, 22, 80, 65, 8]
    price.sort()
    print("El nùmero menor es " + str(price[0]))
    print("El nùmero mayor es " + str(price[-1]))

def ejercicio11():
    vec1 = (1,2,3)
    vec2 =  (-1,0,2)
    large = len(vec1)    #da igual que variable ya qua ambas tuplas son iguals de grandes
    producto_escalar = 0
    #producto escalar: la suma de las múltiplicaciones de cada dígito y posición del vector 1 por vector 2
    for i in range(large):
        producto_escalar = producto_escalar + (vec1[i] * vec2[i])
        i+=1
    print(producto_escalar)

def ejercicio12():
    a = [[1,2,3],[4,5,6]]
    b = [[-1,0],[0,1],[1,1]]
    
    res = [[0,0],[0,0]]
    
    for i in range(len(a)):   #i valdra 1 y 2
        for j in range(len(b[0])):   #j valdra 1 y 2
            for k in range(len(b)):  #k valdra 1,2 y 3
                res[i][j] += a[i][k] * b[k][j]
    for i in range(len(res)):
        res[i] = list(res[i])
    res = list(res)
    for i in range(len(res)):
        print(res[i])

#end ejercicio12   








