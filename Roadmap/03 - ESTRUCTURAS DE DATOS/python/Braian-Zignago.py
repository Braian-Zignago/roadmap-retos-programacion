""""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

"""
Estructuras de datos en Python
"""

# 1. Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.

#Lista: Conjuntos de elementos de datos mutables. O sea, se pueden cambiar y hacer varias operaciones.
my_list = [1, 2, 3, 'hello', True]
print(f'My list default: {my_list}')

my_list.append('world')             # Inserta un elemento al final de la lista
my_list.insert(4, False)         # Inserta un elemento en la posicion indicada
print(f'My list whit append and insert: {my_list}')

my_list.remove('hello')             # Elimina el primer elemento en la lista con ese valor
print(f'My list whit remove: {my_list}')

my_list.pop()                       # Devuelve y saca de la lista el ultimo elemento
print(f'My list whit pop: {my_list}')   

my_list.sort()                      # Ordena la lista
print(f'My list whit sort: {my_list}')

print(f'My list whit index "2": {my_list.index(2)}')    #muestra el index de un elemento en la lista

print(f'My list whit count "2": {my_list.count(2)}')    #muestra cuantos mismos elementos hay

my_list.extend([4,5,6])
print(f'My list whit extend: {my_list}')    #añade un conjunto de elementos al final de la lista

print(" ")
#Tupla : Conjuntos de elementos de datos inmutables. O sea, no se pueden cambiar. Ya que usan una almacenamiento en la memoria de forma linear y no se pueden mover.
my_tuple = (1, 2, 3, 'hello', False, 'python')
print(f'My tuple: {my_tuple}')

print(" ")
""""
#Sets: Conjuntos de elementos buenisimos para almacenar grandes cantidades de datos. 
# PERO NO SON INDEXABLES, LOS INDICES CAMBIAN A CADA ITERACION.
Almacenan elementos unicos a traves de su hash, NO SE PERMITEN DATOS DUPLICADOS.
"""

my_set = {'Braian', 'Zignago', 36}
print(f'my set: {my_set}')
my_set.add('braianifsul@gmail.com')
print(f"My set whit add: {my_set}")


print(" ")
"""
#Dictionaries: 
"""
my_dict = {
    'name' : 'Braian',
    'last_name' : 'Zignago',
    'age' : '23',
    'ocupation' : 'Student'
}
print(f'My dict: {my_dict}')

my_dict['email'] = 'braianifsul@gmail.com' # Insercion
print(f'My dict whit add: {my_dict}')

print(f'My dict whit select "name": {my_dict["name"]}') # Acceso

my_dict['age']  = '24' # Actualizacion
print(f'My dict whit update: {my_dict}')

del my_dict['ocupation'] # Eliminacion
print(f'My dict whit delete: {my_dict}')


print("""

Ejercicio:  * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.

 * - Cada contacto debe tener un nombre y un número de teléfono.

 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.

 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).

 * - También se debe proponer una operación de finalización del programa
""")


agenda: dict = {}
def buscar():
    global agenda
    name = input (" Ingrese el nombre del contacto que desea Buscar: ")
    if name in agenda:
            print (f"{name} : {agenda[name]}")
    else:
        print (" El contacto no se encuentra en la agenda")
        ag = input ("Desea agregarlo S/N: ")
        ag = ag.upper()
        if ag == "S":
            agregar(name)
        elif ag == "N":
            pass

def agregar(name = " "):
    global agenda
    if name == " ":
        name = input (" Ingrese el nombre del contacto que desea Agregar: ")
    num = input (f" Ingrese el telefono del contacto de {name}: ")
    while True:
        if num.isdigit() and len(num) == 11:
            agenda[name] = num
            break
        else:
            msg = "!!!!El número de teléfono debe tener menos de 11 digitos y ser numérico.!!!!!!!"
            print (msg.upper())
            num = input (" Ingrese nuevamente el telefono del contacto que desea Agregar: ")
    print (agenda)
    print (f"El contacto {name} se ha ingresado correctamente")


def actualizar():
    global agenda
    name = input ("Ingrese el nombre del contacto que quiere actualizar: ")
    if name not in agenda:
        print (" El contacto no se encuentra en la agenda")
        ag = input (f""" 1! Actulizar otro contacto   (Any key for exit)  2! Agregar el contacto {name}: """)
        match ag:
            case '1': actualizar()
            case '2': agregar(name)
            case _: pass
    else:
        while True:
            num = input (f"Ingrese el nuevo numero de {name} : ")
            if num.isdigit() and len(num) == 11:
                agenda[name] = num
                print (f"El contacto {name} se ha actualizado correctamente")
                break
            else:
                msg = "!!!!El número de teléfono debe tener menos de 11 digitos y ser numérico.!!!!!!!"
                print (msg.upper())
                num = input (" Ingrese nuevamente el telefono del contacto que desea Actualizar: ")

def eliminar():
    global agenda
    name = input ("Ingrese el nombre del contacto que quiere eliminar: ")
    if name not in agenda:
        print (" El contacto no se encuentra en la agenda")
        ag = input (f""" 1! Eliminar otro contacto   (Any key for exit)  2! Agregar el contacto {name}: """)
        match ag:
            case '1': eliminar()
            case '2': agregar(name)
            case _: pass
    else:
        del agenda[name]
        print (f"El contacto {name} se ha eliminado correctamente")

def listar():
    global agenda
    for value, element in agenda.items():
        print (f"{value} : {element}")

while True:
    print("""
    1 ! Buscar \n 
    2 ! Agregar \n
    3 ! Actualizar\n
    4 ! Eliminar\n
    5 ! Lista\n
    --->Any key for exit<---""")
    opcion = input("Ingrese una opcion: ")

    match opcion:
        case '1': print(f'1 Buscar {buscar()}')
        case '2': print(f'2 Agregar {agregar()}')
        case '3': print(f'3 Actualizar {actualizar()}')
        case '4': print(f'4 Eliminar {eliminar()}')
        case '5': print(f'Listar agenda:\n {listar()}')
        case _: break
