# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
# Consulta de datos

# Nombre completo
print('Ingrese por consola su nombre completo:')
nombre_completo = str(input())

# DNI
print('Ingrese por consola su DNI:')
dni = int(input())

# Edad
print('Ingrese por consola su Edad:')
edad = int(input())

# Altura
print('Ingrese por consola su altura en metros y centimetros:')
altura = float(input())

# imprimir nombre completo y el DNI
print('Nombre Completo:', nombre_completo, ' DNI:',dni)

# imprimir nombre completo, edad, altura
print('Nombre Completo:', nombre_completo, ' Edad:', edad, ' Altura:', altura)
