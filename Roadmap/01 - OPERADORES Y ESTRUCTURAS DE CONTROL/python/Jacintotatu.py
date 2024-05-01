""" * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo."""

#operadores aritmeticos

print(f'Suma 12 + 8 = {12 + 8}')
print(f'Resta 12 - 8 = {12 - 8}')
print(f'Multiplicación 12 x 8 = {12 * 8}')
print(f'Division entera 12 / 4 = {12 // 4}')
print(f'Division con decimales 12 / 4 = {12 / 5}')
print(f'Módulo (resto) 12 / 5 = {12 % 5}')
print(f'exponente 12 elevado a 2 = {12 ** 2}')

#operadores de asignación

#el operador '=' asigna un valor a una variable

variable = 100

variable += 1   #asigna y suma 1 al valor de la variable
print(variable)

variable -= 3  #asigna y resta 3 al valor de la variable 
print(variable)

variable *= 2  #asigna y multiplica por 2 el valor de la variable
print(variable)

variable //= 2  #asigna y divide entre 2 el valor de la variable
print(variable) 

variable /= 5 #asigna y divide con decimales entre 5 el valor de la variable
print(variable)

variable %= 2 #asigna y divide entre 2 el valor de la variable para obtener el resto.
print(variable)

