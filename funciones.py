def conversacion(mensaje):
    print("Hola!", mensaje)


opcion = int(input("Elige la opción (1,2,3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("Elegiste la opcion incorrecta")
