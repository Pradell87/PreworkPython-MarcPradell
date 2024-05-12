'''
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''

print("Introduce una palabra:")
palabra = input()
vocales = "aeiouAEIOU"
nVocales = 0

for letra in palabra:
    if letra in vocales:
      nVocales += 1
    
print("El número de vocales en la palabra", palabra, "es:", nVocales)