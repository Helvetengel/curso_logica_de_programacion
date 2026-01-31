#Listas
my_list = ["Lexi", "Charson", "Aiden", "Aina", "Evyler", "Onney"] #conjuntos ordenados de datos
print(my_list)
my_list.append("Hellen") #añade un elemento al final de la lista
print(my_list)
my_list.remove("Hellen") #elimina un elemento de la lista
print(my_list)
print(my_list[1]) #acceso a un dato
my_list[3] = "AE" #cambia un elemento determinado
print(my_list)
my_list.sort() #ordena alfabéticamente la lista
print(my_list)


#Tuplas
my_tuple = ("Lexi", "Helvetengel", "@helvetengel", "23") #Listas inmutables
print(my_tuple[2]) #acceso a un dato
print(sorted(my_tuple)) #ordena la tupla y devuelve una lista


#Sets
my_set = {"Lexi", "Helvetengel", "@helvetengel", "23"} #Listas desordenadas, no tienen operación de acceso y no permiten datos duplicados
my_set.add("sashabelana@gmail.com") #agregar datos
my_set.remove("Lexi") #eliminar datos
print(my_set)


#Diccionarios
my_dict: dict = {"name":"Lexi", "surname":"Helvetengel", "alias":"@helvetengel", "age": "23"} #"clave":"valor"
my_dict["name"] #acceso a dato
my_dict["email"] = "sashabelana@gmail.com" #agregar datos (clave:valor), si el dato no existe, lo inserta
my_dict["email"] = "wisdomsywar@protonmail.com" #actualizar datos
del my_dict["surname"] #eliminar datos
my_dict = dict(sorted(my_dict.items())) #ordenación: se ordena con sorted(), pero solo las claves. Luego se usa .items para ordenar junto con las claves. Devuelve una lista de tuplas, que se convierten de nuevo a diccionario con dict()




#DIFICULTAD EXTRA

def agenda():
    agenda_de_contactos: dict = {}
    while True:
        print("1 - Búsqueda")
        print("2 - Inserción")
        print("3 - Actualización")
        print("4 - Eliminación")
        print("5 - Salir del programa")
        print("Escriba el número de la operación que desea realizar:")
        numero = input()
        if numero == "1":
            print("Escriba el número del contacto a buscar:")
            eleccion = input()
            if type(eleccion) != int or len(eleccion) > 11:
                print("Ingrese un número entero de 11 o menos dígitos")
        elif numero == "2":
            print("Escriba el número del contacto a insertar")
            eleccion = input()
            if type(eleccion) != int or len(eleccion) > 11:
                print("Ingrese un número entero de 11 o menos dígitos")
        elif numero == "3":
            print("Escriba el número del contacto a actualizar")
            eleccion = input()
            if type(eleccion) != int or len(eleccion) > 11:
                print("Ingrese un número entero de 11 o menos dígitos")
        elif numero == "4":
            print("Escriba el número del contacto a eliminar")
            eleccion = input()
            if type(eleccion) != int or len(eleccion) > 11:
                print("Ingrese un número entero de 11 o menos dígitos")
        elif numero == "5":
            print("Programa finalizado")
            break
        else:
            print("Opción rechazada")
agenda()