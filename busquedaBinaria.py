from array import *
maxrange=5
listaVectores=array('i', range(maxrange))

def es_entero(num):
    try:
        int(num)
        return True
    except Exception as e:
        return False

def ingresar_numeros(mensaje):
    num=input(mensaje).strip()
    if es_entero(num):
        return int(num)
    else:
        print(f"Error: {num} no es un nùmero vàlido")

def busqueda_binaria(array, itemSeleccionado):
    izquierda, derecha = 0, len(array)-1
    while izquierda <= derecha:
        media = (izquierda + derecha) // 2

        if array[media] == itemSeleccionado:
            return media
        elif array[media] < itemSeleccionado:
            izquierda = media + 1
        else:
            derecha = media - 1

    return -1

def menuLista():
    print("\n------------------------------------------")
    print("Menú de opciones:")
    print("1 - Lista de números ")
    print("2 - Búsqueda binaria ")
    print("3 - Salir ")
    print("------------------------------------------\n")

def menu():
    while True:
        opcion = input("\nIngrese una opción: ")
        if opcion in ['1', '2', '3']:
            return opcion
        else:
            print("\nError: Debe ingresar una opción válida")


def lista_numeros(array_numeros):
    for i in range(maxrange):
        if i==0:
            str=f"[{array_numeros[i]}, "
        elif i==maxrange-1:
            str=f"{array_numeros[i]}]\n"
        else:
            str = f"{array_numeros[i]}, "
        print(str, end="")

def lista_opciones(op):
    if op== '1':
        print("\nLista de números: ")
        lista_numeros(listaVectores)
    elif op == '2':
        valor = ingresar_numeros("\n¿Que número quiere buscar?: ")
        resultado = busqueda_binaria(listaVectores, valor)
        if resultado != -1:
            print(f"El número {valor} se encuentra en la posición {resultado+1}")
        else:
            print(f"El número {valor} no existe dentro de los parametros de la lista.")
    elif op == '3':
        print("Fin del programa.")



for i in range(maxrange):
    num=""
    while not (es_entero(num)):
        num=ingresar_numeros(f"Ingrese el {i+1}ª nùmero: ")
    listaVectores[i]=num

listaVectores = array('i', sorted(listaVectores))
opcion=""
menuLista()
while opcion != '3':
    opcion = menu()
    lista_opciones(opcion)


