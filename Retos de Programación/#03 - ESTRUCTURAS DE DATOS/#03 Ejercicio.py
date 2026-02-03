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
    agenda_de_contactos: dict = {"Lexi":"294294294", "Charson":"666666666", "Sywar":"4815162342"}
    
    while True:
        print("***AGENDA***") #título
        print("1 - Búsqueda")
        print("2 - Inserción")
        print("3 - Actualización")
        print("4 - Eliminación")
        print("5 - Salir del programa")
        print("Escriba el número de la operación que desea realizar:")
        numero = int(input())

        match numero:
            case 1:
                nombre = input("Ingrese el nombre del contacto que quiera buscar: ")
                if nombre in agenda_de_contactos:
                    print(f"El número de {nombre} es: {agenda_de_contactos[nombre]}")
                else:
                    print("Contacto no encontrado")

            case 2:
                nombre = input("Introduzca el nombre de su nuevo contacto: ")
                numero_de_telefono = input("Introduzca el número de su nuevo contacto: ")
                if type(numero_de_telefono) != int and len(numero_de_telefono) > 11:
                    print("Error, por favor ingrese un valor numérico menor a 11 dígitos")
                else:
                    print("Contacto guardado con éxito")
                agenda_de_contactos[nombre] = numero_de_telefono

            case 3:
               nombre = input("Ingrese el nombre del contacto a actualizar: ")
               nuevo_nom = input("Introduzca el nuevo nombre del contacto: ")
               nuevo_num = input("Introduzca el nuevo número del contacto: ")
               if type(nuevo_num) != int and len(nuevo_num) > 11:
                    print("Error, por favor ingrese un valor numérico menor a 11 dígitos")
               else:
                print("Contacto actualizado con éxito")
                del agenda_de_contactos[nombre]
               agenda_de_contactos[nuevo_nom] = nuevo_num

            case 4:
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                del agenda_de_contactos[nombre]
                print("Contacto eliminado con éxito")

            case 5:
                print("Programa finalizado")
                break
            case _:
                print("Opción rechazada")

agenda()