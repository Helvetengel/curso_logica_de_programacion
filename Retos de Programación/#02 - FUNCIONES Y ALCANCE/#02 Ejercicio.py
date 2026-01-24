#FUNCIONES

#Función simple, sin parámetros ni retorno
def greet():
    print("Hola, Python!")  #Bloque de código dentro de la función
greet()                     #Llama a la función y ejecuta el bloque de código

#Función con 1 parámetro
def arg_greet(name):
    print(f"Hola, {name}!")
arg_greet("Lexi")

#Función con varios parámetros
def args_greet(greet, name):
    print(f"{greet}, {name}!")
args_greet("Hi", "Lexi")
args_greet(name="Lexi", greet="Hi")     #indica orden aunque varíe la posición

#Función con retorno
def return_greet():
    return ("Hola, Python!")
print(return_greet())

#Función con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"
greet, name = multiple_return_greet()
print(greet)
print(name)

#Función con parámetros y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}!"
print(return_args_greet("Hi", "Lexi"))

#Con un número variable de parámetros
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
variable_arg_greet("Lexi", "Charson", "Aiden", "Aina") # "*" indica que se pasa más de una variable separadas por comas

#Función con parámetro predeterminado/default
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")
default_arg_greet("Lexi")   #Hola, Lexi!
default_arg_greet()         #Hola, Python! (default)

#Función con un número variable de parámetros con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola,{value}({key})!")
variable_key_arg_greet(
    language = "Python",
    name = "Lexi",
    alias = "Helvetengel",
    age = "18"
)


#Función dentro de una función
def outside():
    def inside():
        print("Función interna")
    inside()
    print("Función externa")
outside()


#Función ya creada en el lenguaje (built-in)
print(len("Lexi"))     #longitud del dato (4)
print(type("Lexi"))    #tipo del dato (string/str)
print("Lexi".upper())  #pone los datos en mayúscula (LEXI)


#Variable global - Variable local
global_var = "Python"
def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")
print(global_var)
#print(local_var) NO SE PUEDE ACCEDER DESDE FUERA DE LA FUNCIÓN
hello_python()



#DIFICULTAD EXTRA

def fun_num(str1, str2)->int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(str1 + str2)
        elif number % 3 == 0:
            print(str1)
        elif number % 5 == 0:
            print(str2)
        else:
            print(number)
            count += 1
    return count
print(fun_num("Text 1", "Text 2"))         #Ejercicio Fizz Buzz