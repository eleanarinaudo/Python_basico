def conversor(tipo_pesos, valor_dolar):
    pesos = input(f"¿Cuantos pesos {tipo_pesos} tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(f"Tienes $ {dolares} dolares")


menu = """
Bienvenido al conversor de monedas a dolares 💰

1 - Peso Colombianos
2 - Peso Argentinos 
3 - Pesos Mexicanos

Elige una opción: 
"""

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3875)

elif opcion == "2":
    conversor("argentinos", 75)
elif opcion == "3":
    conversor("mexicanos", 45)
else:
    print("Ingresa una opcion correcta por favor")


# pesos = input("Cuantos dolares coolombianos tienes?: ")
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# print(f"Tienes $ {dolares} dolares" )
