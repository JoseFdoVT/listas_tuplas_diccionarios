# 1.Filtrar elementos: Utiliza listas y comprensiones para filtrar elementos basados en ciertos criterios. Por ejemplo, puedes filtrar una lista de números para obtener solo los números pares o impares, o filtrar una lista de cadenas para obtener solo las que contengan ciertas letras.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares) 

cadenas = ["manzana", "banana", "cereza", "durazno", "kiwi"]
cadenas_con_a = [cadena for cadena in cadenas if 'a' in cadena]
print(cadenas_con_a)  


# 2. Operaciones matemáticas: Utiliza listas o tuplas para realizar operaciones matemáticas en conjuntos de datos. Por ejemplo, puedes sumar los elementos de una lista, obtener el producto de una tupla o calcular la media de una lista de números.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = sum(numeros)
print(suma)  

from functools import reduce

numeros = (1, 2, 3, 4, 5)
producto = reduce(lambda x, y: x * y, numeros)
print(producto) 

numeros = [1, 2, 3, 4, 5]
media = sum(numeros) / len(numeros)
print(media)  




# 3.Acceder y modificar elementos: Utiliza índices para acceder a elementos específicos en listas, tuplas o diccionarios. También puedes modificar los valores de los elementos si es necesario.
lista = [10, 20, 30, 40, 50]
print(lista[2]) 
lista[2] = 35
print(lista) 

tupla = (10, 20, 30, 40, 50)
print(tupla[2])  


diccionario = {'a': 1, 'b': 2, 'c': 3}
print(diccionario['b'])  

diccionario['b'] = 20
print(diccionario) 
