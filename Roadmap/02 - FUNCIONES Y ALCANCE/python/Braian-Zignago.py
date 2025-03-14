""""
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

num_two = 10
num_one: int = 12
# Función sin parámetros, ni retorno
def greet():
    print("Hola soy Braian")

greet()

# Funcion con mas de un parametro

# Función sin parámetros, con retorno
def suma():
    global num_one
    num_two = 5
    return num_one + num_two
print(f"suma {suma()}")

# Función con parámetros, sin retorno
def resta(num_one, num_two):
    print(num_one - num_two)

resta(3, 5)


# Función con parámetros, con retorno
def division(num_one, num_two):
    resultado = num_one / num_two
    return resultado

print(f"El resultado de la division 3 / 5 es: {division(3, 5)}")

def arg_greet(adjetivo, objet):
    return f"Hola {adjetivo} de {objet}"

print(arg_greet("pedazo", "mierda"))

#Funcion con mas de un RETORNO
def list_of_market():
    return "zanahoria " , "tomate " , "lechuga"
for i, elemento in enumerate(list_of_market(),start=1):
    print(f'{i}: {elemento}')

#Funcion Con numero variables de argumentos
def sumar(*numeros):
    for number in numeros:
        print(f"The number this time is: {number}")

sumar(1, 2, 3, 4, 5,2,2,2,2,2)

#Funcion con diccionarios

def variable_key_arg_greet(**greets):
    for key, value in greets.items():
        print(f"{key}: {value}!")

variable_key_arg_greet(language="Python", name="Braian" , alias="Ansinaaa", age=22)


"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola Python!")
    inner_function()

outer_function()


""""
Exercicio Extra

"""
def multiplos(text1, text2):
    sum = 0 
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{text1} {text2}")
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            sum += 1
    return sum

text_1, text_2 = input("Ingrese el texto 1: "), input("Ingrese el texto 2: ")
print(f"Se imprimio los numeros {multiplos(text_1, text_2)} veces")
