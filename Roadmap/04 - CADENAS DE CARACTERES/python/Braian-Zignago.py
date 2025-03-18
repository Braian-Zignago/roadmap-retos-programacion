""""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""


""""
Operaciones con cadenas de caracteres
"""

s1 = "Hello"
s2 = "Python"

#Concatenacion
print(s1 + ", " + s2)

#Repeticion 
print(s1 * 3)

#Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

#Longitud
print(len(s2))

#Slicing    
print(s2[1:])

#Busqueda
print("a" in s1)
print("i" in s1)

#Reemplazo
print(s1.replace("e", "a"))
print(s1.replace("l", "L"))

#División
print(s1.split("l"))

#Unión
print(s1 + " " + s2)

#Interpolación
name = "Daniel"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

#Mayusculas y minusculas
print(s1.upper())
print(s1.lower())
print(s2.title())
print(s2.capitalize())

#Eliminar espacios
s3 = "   Hello Python   "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

#Busqueda al principio y al final
print(s1.startswith("H"))
print(s1.endswith("o"))

""""
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
  recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
  interpolación, verificación..."""

print("""\n\n\n---------------------------Ejercicio--------------------------------------------\n\n\n""")



def check(word1: str, word2: str):

    # Palíndromos
    print(f'{word1} es un palindromo? {word1 == word1[::-1]}')
    print(f'{word2} es un palindromo? {word2 == word2[::-1]}')

    # Anagramas
    print(f"{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas
    print(f"{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"{word2} es un isograma?: {len(word2) == len(set(word2))}")

check("radar","quesoqueso")

