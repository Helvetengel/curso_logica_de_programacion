#OPERADORES
#Operadores Aritméticos
print(f"{10 + 4}")    #suma
print(f"{10 - 4}")    #resta
print(f"{10 * 4}")    #multiplicación
print(f"{10 / 4}")    #división
print(f"{10 % 4}")    #módulo (resto de la división)
print(f"{10 ** 4}")   #exponente
print(f"{10 // 4}")   #división entera (resultado sin coma)


#Operadores de Asignación
number = 294    #asignación
print(number)
number += 6     #suma y asignación
print(number)
number -= 6     #resta y asignación
print(number)
number *= 2     #multiplicación y asignación
print(number)
number /= 2     #división y asignación
print(number)
number %= 4     #módulo y asignación
print(number)
number **= 2    #exponente y asignación
print(number)
number //= 2    #división entera y asignación
print(number)
'''number &= 4
#number |= 4
#number ^= 4
#number >>= 4
#number <<= 4
#number := 4''' #???


#Operadores de Comparación
print(f"{10 == 4}")      #igualdad (FALSE)
print(f"{10 != 4}")      #desigualdad (TRUE)
print(f"{10 > 4}")       #mayor que (TRUE)
print(f"{10 < 4}")       #menor que (FALSE)
print(f"{10 >= 10}")     #mayor o igual que (TRUE)
print(f"{10 <= 4}")      #menor o igual que (FALSE)


#Operadores Lógicos
print(f"{10 + 4 == 14 and 6 - 2 == 4}")     #AND && (TRUE)
print(f"{10 + 4 == 15 or 6 - 2 == 4}")      #OR || (TRUE)
print(f"{not 10 - 2 == 6}")                 #NOT ! (TRUE)


#Operadores de Identidad
another_number = 147
print(f"{number is another_number}")        #(FALSE)
another_number = number
print(f"{another_number is number}")        #(TRUE)
print(f"{number is not another_number}")    #(FALSE)


#Operadores de Pertenencia
print(f"{"e" in "Lexi"}")       #(TRUE)
print(f"{"i" not in "Lexi"}")   #(FALSE)


#Operadores de Bit
a = 10  #1010
b = 3   #0011
print(f"{10 & 3}")  #AND (0010)
print(f"{10 | 3}")  #OR (1011)
print(f"{10 ^ 3}")  #XOR (1001)
print(f"{~ 10}")    #NOT (-11)
print(f"{10 >> 2}") #Desplazamiento a la derecha (0010)
print(f"{10 << 2}") #Desplazamiento a la izquierda (101000)




#ESTRUCTURAS DE CONTROL

#Condicionales
string = "Lexi"

if string == "Lexi":                                #if statement
    print("string es 'Lexi'")
elif string == "Helvetengel":                       #else if
    print("string es 'Helvetengel'")
else:                                               #else statement
    print("string no es 'Lexi' ni 'Helvetengel'")


#Iterativas
for i in range(11):     #for loop
    print(i)

i = 0

while i <= 10:          #while loop
    print(i)
    i += 1


#Manejo de excepciones
try:                    #prueba el código
    print(10 / 0)
except:                 #si se produce error, usa la siguiente instrucción
    print("Error")
finally:                #se ejecuta haya o no error
    print("End")



#DIFICULTAD EXTRA
print("Ejercicio Extra:")
i = 10
for i in range(56):
    while i >= 10 and i < 56:
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)
        while i < 56:
         i += 1