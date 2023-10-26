class Volkswagen:

    modelos_volkswagen = [
        "Volkswagen Golf",
        "Volkswagen Passat",
        "Volkswagen Tiguan",
        "Volkswagen Jetta",
        "Volkswagen Atlas",
        "Volkswagen Arteon",
        "Volkswagen Polo",
        "Volkswagen Beetle",
        "Volkswagen Touareg",
        "Volkswagen ID.4 (eléctrico)",
        # Puedes añadir más modelos de Volkswagen aquí
    ]

    def __init__(self):
        pass

    def elegir_volkswagen(self):
        while True:
            print()
            print("Escoja el modelo de Volkswagen que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehículo seleccionado Volkswagen Golf")
            elif opcion == "2":
               print("Vehículo seleccionado Volkswagen Passat")
            elif opcion == "3":
               print("Vehículo seleccionado Volkswagen Tiguan")
            elif opcion == "4":
               print("Vehículo seleccionado Volkswagen Jetta")
            elif opcion == "5":
               print("Vehículo seleccionado Volkswagen Atlas")
            elif opcion == "6":
               print("Vehículo seleccionado Volkswagen Arteon")
            elif opcion == "7":
               print("Vehículo seleccionado Volkswagen Polo")
            elif opcion == "8":
               print("Vehículo seleccionado Volkswagen Beetle")
            elif opcion == "9":
               print("Vehículo seleccionado Volkswagen Touareg")
            elif opcion == "10":
               print("Vehículo seleccionado Volkswagen ID.4 (eléctrico)")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
