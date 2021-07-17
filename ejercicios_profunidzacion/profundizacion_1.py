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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# Ingresar numero real 1
print('Ingrese por consola un numero real 1:')
numero_1 = float(input())

# Ingresar numero real 2
print('Ingrese por consola un numero real 2:')
numero_2 = float(input())

# Suma
suma = numero_1 + numero_2
print('La suma de',numero_1, 'y',numero_2,'es:',suma)

# Resta
resta = numero_1 - numero_2
print('La resta de',numero_1, 'y',numero_2,'es:',resta)

# Multiplicacion
multiplicacion = numero_1 * numero_2
print('La multiplicacion de',numero_1, 'por',numero_2,'es:',multiplicacion)

# Division
division = numero_1 / numero_2
print('La division de',numero_1, 'entre',numero_2,'es:',division)

# Exponente
exponente = numero_1 ** numero_2
print('La potencia de',numero_1, 'a',numero_2,'es:',exponente)
