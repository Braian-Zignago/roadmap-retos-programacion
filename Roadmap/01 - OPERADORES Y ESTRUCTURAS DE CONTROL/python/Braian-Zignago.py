"""
 * EJERCICIO:
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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """
"""
Operadores
"""

# Aritméticos
print('--------------------------------------------------------')
print("Operadores Aritméticos: ")
print(f'Suma: 10 + 3 = {10 + 3}')
print(f'Resta: 10 - 3 = {10 - 3}')
print(f'Multiplicación: 10 * 3 = {10 * 3}')
print(f'División: 10 / 3 = {10 / 3}')
print(f'Módulo: 10 % 3 = {10 % 3}')
print(f'Exponente: 10 ** 3 = {10 ** 3}')
print(f'División entera: 10 // 3 = {10 // 3}')  

# Comparación
print('--------------------------------------------------------')
print("Operadores de Comparación: ")
print(f'Mayor que: 10 > 3 = {10 > 3}')
print(f'Menor que: 10 < 3 = {10 < 3}')
print(f'Mayor o igual que: 10 >= 3 = {10 >= 3}')
print(f'Menor o igual que: 10 <= 3 = {10 <= 3}')
print(f'Igual a: 10 == 3 = {10 == 3}')
print(f'Diferente de: 10 != 3 = {10 != 3}')

#Logicos
print('--------------------------------------------------------')
print("Operadores Lógicos: ")
print(f'AND &&: 10 + 20 = 30 and 10 - 20 = -10 es: {10 + 20 == 30 and 10 - 20 == -10 }')
print(f'OR ||: 10 + 23 = 30 or 10 - 20 = -10 es: {10 + 23 == 30 or 10 - 20 == -10 }')
print(f'NOT !: not 10 + 23 = 30 es: {not 10 + 23 == 30 }')

#ASIGNACION
print('--------------------------------------------------------')
print("Operadores de Asignación: ")
my_name = 'Braian' # asignacion =
my_name += ' Zignago' # concatenacion: suma y asignacion con = 

#IDENTIDAD
print('--------------------------------------------------------')
print("Operadores de Identidad: ")
my_new_name = 'Braian Zignago'
print(f'my_new_name es my_name: {my_new_name is my_name}')
print(f'my_new_name no es my_name: {my_new_name is not my_name}')

#Pertenencia
print('--------------------------------------------------------')
print("Operadores de Pertenencia: ")
print(f"'Br' not in my_name: {'Br' not in my_name}")
print(f"'Br' in my_name: {'Br' in my_name}")

#BITS
print('--------------------------------------------------------')
print("Operadores de Bits: ")
print(f'10 & 3 = {10 & 3}')
print(f'10 | 3 = {10 | 3}')
print(f'10 ^ 3 = {10 ^ 3}')
print(f'~10 = {~10}')
print(f'10 << 2 = {10 << 2}')
print(f'10 >> 2 = {10 >> 2}')

"""ESTRUCTURAS DE CONTROL"""

#CONDICIONALES
my_name = 'Braian'
if my_name == 'Braian Zignago':
    print('Mi nombre es Braian Zignago')
elif my_name == 'Braian':
    print('Mi nombre es Braian')
else:
    print('Mi nombre no es Braian Zignago')

#ITERATIVAS
for i in range(5):
    print(f'i = {i}')

#WHILE
y = 0
while y <=  5:
    print(f'y = {y}')
    y += 1

#EXCEPCIONES
try:
    print(f'10 / 0 = {10 / 0}')
except Exception as e:
    print(f'Error: {e} ({type(e).__name__})')    
finally:
    print('Ha finalizado la ejecución de excepciones')

"""EXTRA"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(i)