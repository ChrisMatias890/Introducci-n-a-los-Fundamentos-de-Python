## Christian Matias Alvarez
## COMP315 - C4
## Laboratorio Manipulación de Listas
## 21 de mayo de 2025

#Función Main
#---------------------------------------------------------------#
def Main():
    numeros = []
    numero_par = []
    string = input("Introduce una cantidad de números separado por un espacio: ")
    numero = string.split(".")
    

    for i in numero:
        numeros.append(int(i))

    #Ciclo para sacar numeros pares
    for pares in numeros:
        if pares % 2 == 0:
            numero_par.append(pares)
   
    print(f"{"=" * 10}Registros de: {numeros} {"=" * 10}")
    print(f"Numeros sumados: {sum(numeros)}")
    print(f"Valor máximo: {max(numeros)}")
    print(f"Valor mínimo: {min(numeros)}")
    print(f"Promedio: {sum(numeros) / len(numeros)}")
    print(f"Lista sin duplicados: {set(numeros)}")
    print(f"Lista Ordenada: {sorted(numeros)}")
    print(f"Numeros pares: {numero_par}")



#---------------------------------------------------------------#

#Llamando la función Main
Main()