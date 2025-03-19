""""
#05 /*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""

""""
Valor y Referencia
"""

#Tipo de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
print(my_int_a)
print(my_int_b)

# Tipo de dato por referencia 
"""
    Cuando se iguala una lista a otra, se copia la referencia y no el valor en si. La referencia equivale al valor de memoria. 
Por eso si cambiamos el valor de una, va cambiar el valor de la otra"""

my_list_a = [10, 20]
my_list_b = [30, 40]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# funciones con dato por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print (my_int)

my_int_func(my_int_c)
print(my_int_c)

my_list_c = [10, 20]

def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_func(my_list_c)
print(my_list_c)





print("\n\n---------------------------------Ejercicio---------------------------------\n\n")

#Intercambio en dato tipo valor
number1 = 10
number2 = 5

def intercambio_val(value1, value2) -> tuple:
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2

print(f"Valores originales: {number1}, {number2}")
print(f"Valores intercambiados: {intercambio_val(number1, number2)}")

#Intercambio en dato tipo referencia
list1 = [10, 5]
list2 = [30, 15]


def intercambio_ref(value1, value2) -> tuple:
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2

print(f"Valores originales: {list1}, {list2}")
print(f"Valores intercambiados: {intercambio_ref(list1, list2)}")

