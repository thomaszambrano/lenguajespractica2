class Renault:

    modelos_renault = [
        "Renault Clio",
        "Renault Captur",
        "Renault Megane",
        "Renault Scenic",
        "Renault Kadjar",
        "Renault Zoe (eléctrico)",
        "Renault Twingo",
        "Renault Duster",
        "Renault Koleos",
        "Renault Talisman",
        # Puedes añadir más modelos de Renault aquí
    ]

    def __init__(self):
        pass

    def elegir_renault(self):
        while True:
            print()
            print("Escoja el modelo de Renault que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehículo seleccionado Renault Clio")
            elif opcion == "2":
               print("Vehículo seleccionado Renault Captur")
            elif opcion == "3":
               print("Vehículo seleccionado Renault Megane")
            elif opcion == "4":
               print("Vehículo seleccionado Renault Scenic")
            elif opcion == "5":
               print("Vehículo seleccionado Renault Kadjar")
            elif opcion == "6":
               print("Vehículo seleccionado Renault Zoe (eléctrico)")
            elif opcion == "7":
               print("Vehículo seleccionado Renault Twingo")
            elif opcion == "8":
               print("Vehículo seleccionado Renault Duster")
            elif opcion == "9":
               print("Vehículo seleccionado Renault Koleos")
            elif opcion == "10":
               print("Vehículo seleccionado Renault Talisman")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
