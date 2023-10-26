class Alquilados:
    #ñadir listas de marca, modelo y año
    def __init__(self) -> None:
       pass

    def carros_alquilados(self):
         while True:
            print()
            print("Lista de vehiculos alquilados: ")
            print()
            print("1. Lista de vehiculos alquilados")
            print("2. Entregar vehiculo")
            print("3. Volver al menú principal")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Lista de vehiculos alquilados: ")
            elif opcion == "2":
               print("Seleccione uno de los siguientes vehiculos a devolver")
            elif opcion == "3":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")