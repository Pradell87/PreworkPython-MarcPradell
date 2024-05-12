'''
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

lista_numeros = [i for i in range(1, 101)]
suma = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma += numero

print(suma)