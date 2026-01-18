#Operadores Aritméticos
10 + 4    #suma
10 - 4    #resta
10 * 4    #multiplicación
10 / 4    #división
10 % 4    #módulo (resto de la división)
10 ** 4   #exponente
10 // 4   #división entera (resultado sin coma)


#Operadores de Asignación
number = 294    #asignación
number += 6     #suma y asignación
number -= 6     #resta y asignación
number *= 2     #multiplicación y asignación
number /= 2     #división y asignación
number %= 4     #módulo y asignación
number **= 2    #exponente y asignación
number //= 2    #división entera y asignación
'''number &= 4
#number |= 4
#number ^= 4
#number >>= 4
#number <<= 4
#number := 4''' #???


#Operadores de Comparación
10 == 4     #igualdad (FALSE)
10 != 4     #desigualdad (TRUE)
10 > 4      #mayor que (TRUE)
10 < 4      #menor que (FALSE)
10 >= 10     #mayor o igual que (TRUE)
10 <= 4     #menor o igual que (FALSE)


#Operadores Lógicos
10 + 4 == 14 and 6 - 2 == 4     #AND && (TRUE)
10 + 4 == 15 or 6 - 2 == 4      #OR || (TRUE)
not 10 - 2 == 6                 #NOT ! (TRUE)


#Operadores de Identidad
another_number = 147
number is another_number        #(FALSE)
another_number = number
another_number is number        #(TRUE)
number is not another_number    #(FALSE)


#Operadores de Pertenencia
"e" in "Lexi"       #(TRUE)
"i" not in "Lexi"   #(FALSE)


#Operadores de Bit
a = 10  #1010
b = 3   #0011
10 & 3  #AND (0010)
10 | 3  #OR (1011)
10 ^ 3  #XOR (1001)
~ 10    #NOT (-11)
10 >> 2 #Desplazamiento a la derecha (0010)
10 << 2 #Desplazamiento a la izquierda (101000)


