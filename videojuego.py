import random

def run():
    num_aleatorio = random.randint(1, 100)
    num_elegido = int(input("Elige un numero del 1 a 100: "))
    while num_elegido != num_aleatorio:
        if num_elegido < num_aleatorio:
            print("Busca un num mas grande")

        else:
            print("Busca un num mas pequeño")
        num_elegido = int(input("Elige otro numero: "))
    print("Ganaste!!")


if __name__ == "__main__":
    run()
