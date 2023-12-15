# Busqueda Binaria

### Programa realizado en Python, con un ingreso de 5 números que serán añadidos a una lista, despliegue de un menú con la opción de visualizar la lista creada y la busqueda binaria del numero que el usuario quiere en específico.

En el código se visualizarán varias funciones desarrolladas.

- **busqueda_binaria():**

```
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
```

Esta función como lo indica, realizará una busqueda de un valor dentro del array ordenado.
Se utilizarán los parametros de "array" e "itemSeleccionado", representando a la lista creada y al numero que ingresaremos en el input al haber seleccionado la opción en la consola

Las variables izquierda y derecha 
representan los indices de inicio y fin 
que recorreran el array dentro del while, dicho
bucle entrará en ejecución siempre y cuando la variable
izquierda no sea superior a derecha

Se tiene en cuenta que en cada iteración, se calculará el indice "media", del rango actual, en caso de que este llegue a equivaler al elemento que estamos buscando, se devuelve el indice, y se anunciará que se ha encontrado el valor.

*Si el valor en posición media:*

1. Es menor al valor que buscamos: Este puede estar en la mitad derecha del rango.

2. Es mayor al valor que buscamos: Este puede estar en la mitad izquierda del rango.

Se ajustan los indices izquierda y derecha para reducir el rango de busqueda, en vez de recorrer de principio a fin una lista, esta busqueda simplificará las cosas logrando por ejemplo, en lugar de recorrer 9 veces para encontrar un valor, que sean 3.

- **es_entero():**
  
Verifica si la cadena que ingreso al principio, y cuando realizo una busqueda de un número, este verifique que sea un número entero, mediante bloques de código conocidos como Try y Except, para el manejo de errores/excepciones que pueden ocurrir cuando el usuario interactúa con la consola, en caso de que se verifique que todo vaya en orden, se validará el booleano y el valor ingresado se transfomará en un Integer, y retornará para que sea ingresado en el array, en caso de ocurrir lo contrario, se lanzará un mensaje de error al usuario, pidiendo que ingrese un número entero que sea válido

- **ingresar_numeros():**
  
Función realizada bajo la idea de ingresar un número, ya sea bajo la finalidad de añadir un valor al array, o realizar una búsqueda en la misma lista.

- **menuLista():**
  
Es solo una función que imprime las opciones existentes.

- **menu():**
  
La función está desarrollada para solicitar al usuario una opción del menú.
Retornará un valor string, que representará una de las tres opciones existentes, caso contrario (ingreso de un numero menor a 1/mayor a 3, u otro tipo de caracter), se imprime un mensaje de error.

- **lista_numeros():**
  
Se imprime una lista de números bajo el parámetro array_numeros(), la lista de números que se imprime.

- **lista_opciones():**
  
En esta función, se efectúa la opción seleccionada por el usuario, mediante condicionales, de las cuales, básicamente abrirían las puertas a varias de las funciones ya mencionadas para su ejecución
