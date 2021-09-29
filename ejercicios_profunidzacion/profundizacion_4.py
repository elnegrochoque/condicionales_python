# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
texto_1 = str(input('Ingrese la primera palabra:\n'))
texto_2 = str(input('Ingrese la segunda palabra:\n'))
texto_3 = str(input('Ingrese la tercer palabra:\n'))
print("1 - Ordenar por orden alfabético ")
print("2 - Ordenar por cantidad de letras")
opcion = int(input("ingrese opcion: "))
if(opcion == 1):
    if(texto_1 > texto_2):
        if(texto_1 > texto_3):
            if(texto_2 > texto_3):
                print(texto_1)
                print(texto_2)
                print(texto_3)
            else:
                print(texto_1)
                print(texto_3)
                print(texto_2)
        else:
            print(texto_3)
            print(texto_1)
            print(texto_2)
    else:
        if(texto_2 > texto_3):
            if(texto_1 < texto_3):
                
                print(texto_2)
                print(texto_3)
                print(texto_1)
            else:
                print(texto_2)
                print(texto_1)
                print(texto_3)
        else:
            print(texto_3)
            print(texto_2)
            print(texto_1)

if(opcion == 2):
    if(len(texto_1) > len(texto_2)):
        if(len(texto_1) > len(texto_3)):
            if(len(texto_2) > len(texto_3)):
                print(texto_1)
                print(texto_2)
                print(texto_3)
            else:
                print(texto_1)
                print(texto_3)
                print(texto_2)
        else:
            print(texto_3)
            print(texto_1)
            print(texto_2)
    else:
        if(len(texto_2) > len(texto_3)):
            if(len(texto_1) < len(texto_3)):
                print(texto_2)
                print(texto_3)
                print(texto_1)
            else:
                print(texto_2)
                print(texto_1)
                print(texto_3)
        else:
            print(texto_3)
            print(texto_2)
            print(texto_1)
