def run():
    mi_diccionario = {"llave1": 1, "llave2": 2, "llave": 3}
    poblacion_pais = {
        "Argentina": 440000,
        "Brasil": 2100040,
    }
    # for pais in poblacion_pais.keys():
    #     print(pais)
    # for pais in poblacion_pais.values():
    #     print(pais)
    for pais, poblacion in poblacion_pais.items():
        print(f"{pais} tiene {poblacion} habitantes")


if __name__ == "__main__":
    run()
