'''
1.1 Dado el siguiente diccionario, cambia el valor de la clave "edad" a 25.
    persona = {"nombre": "Juan", "edad": 10}
    
1.2 Declara una variable "precio" y asignale el valor 25. Luego, crea una variable "impuesto" y asignale el valor de "Precio" multiplicado por 0.21.
    Muestra ambos valores por consola de esta forma:
    El precio es 25 y el impuesto es 5.25.
    
1.3 Dado el siguiente diccionario, imprime con un print el valor de la calve "apellido".
    persona = {"nombre": "Juan". "apellido": "Pérez"}
    
1.4 Crea un diccionario llamado "producto" que tanga las claves "nombre", "precio" y "cantidad".
Asigna valores a estas claves y luego muestra el diccionario completo por consola.
'''

persona = {"nombre": "Juan", "edad": 10}
persona['edad'] = 30
print(persona)

precio = 25
impuesto = precio * 0.21
print ( "El precio es", precio, "y el impuesto es", impuesto)

persona1 = {"nombre": "Juan", "apellido": "Pérez"}
print(persona1['apellido'])

producto = {"nombre": "Patata", "Precio": 5, "Cantidad": 10}
print(producto) 