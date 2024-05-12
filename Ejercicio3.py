'''
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
'''
print("Introduce tu edad:")
edad = int(input())

if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")