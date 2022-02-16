# Apunte Curso de Python

## Algoritmo

- Es una serie de pasos ordenados para solucionar un problema
- Es Finito (serie limitado)
- No ambiguo 

## Instalación de Herramientas

- Editor de Código (VS Code)
- Consola (cmder)
- Python 3.X
  
## Consola

- Limpiar
  ctrl + L
  o 
  ```bash
    clear 
  ```

- Mover directorios
    - Para mover al directorio anterior:
    ```bash
    cd ..
    ```

    - Ir a un directorio
    ```bash
    cd <nombre_carpeta>
    ```

- Ver los archivos dentro de ese directorio
    ```bash
    ls 
    ```

- Crear directorio
    ```bash
    mkdir  <nombre_carpeta>
    ```
- Crear archivo
    ```bash
    touch <nombre_archivo.firnar>
    ```
## Operadores aritméticos

Activar Python en la consola interactiva

```bash
py 
``` 

- Suma
```bash 
>>> 5 + 5
```

- Division
```bash 
>>> 21 / 5 
>>> 4.2
```

- Dividir entero
```bash 
>>> 21 // 5
>>> 4
```

- Módulo 
```bash 
>>> 21 % 5
>>>  2
```

- Potencia
```bash 
>>> 2**2
>>>  4 
```

## Variable

Es un lugar en memoria (una especie de caja) en el que podemos guardar objetos (números, texto, etc). 

Esta variable posee un identificador o nombre con el cual podemos llamarla cuando la necesitemos.

### Asignación de variables

En Python creamos las variables asignándoles un valor de la siguiente manera:

```python
<identificador> = <valor>
```

En este caso el signo = se lee como “asignar”

para poder imprimir el valor de la variable:

```bash 
py
>>> print(identificador)
```

Reasignación de variables
Podemos en cualquier momento cambiar el valor de nuestra variable volviendo a asignar un valor al mismo identificador

```python
<identificador> = <nuevo_valor>
```

Reglas en el uso de identificadores:
- No pueden empezar con un número.
- Deben estar en minúsculas
- Para separar las palabras usamos el guion bajo: _
- Estas reglas son aplicadas al lenguaje python, en otros lenguajes pueden haber otras reglas.

## Primitivos: Tipos de datos sencillos

![Imagen](https://www.researchgate.net/profile/Pedro_Gomis/publication/325387232/figure/fig4/AS:630680337793025@1527377318263/Figura-8-Tipos-de-datos-El-tipo-de-dato-caracter-no-existe-en-Python-un-caracter.png)

## Convertir un dato a un tipo diferente

- Usamos `input()` para pedirle al usuario que introduzca datos.

```python
<nombre_identificador> = input("Introduce un valor")
```

- `int()` con datos o variables dentro de paréntesis para convertirlo en número entero.
  
```python
<nombre_identificador> = int(input("Introduce un valor"))
```
ó
```python
<nombre_identificador> = input("Introduce un valor")
int(<nombre_identificador>)
```

- `str()` para convertir números tanto decimales como enteros a strings.

```python
str(<nombre_identificador>)
```
## Funciones

![Funciones](https://static.platzi.com/media/user_upload/Funciones-986e7e4c-a885-4e2a-80c6-11dd1665cd06.jpg)

![Funciones](https://static.platzi.com/media/user_upload/Build-int%20functions-e1b3d053-5c76-4ffe-b6b3-5a61e062d77c.jpg)