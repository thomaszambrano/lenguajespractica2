class Kia:

    modelos_kia = [
        "Kia Forte",
        "Kia Optima",
        "Kia Seltos",
        "Kia Sportage",
        "Kia Sorento",
        "Kia Telluride",
        "Kia Rio",
        "Kia Soul",
        "Kia Carnival",
        "Kia Stinger",
        # Puedes añadir más modelos de Kia aquí
    ]

    def __init__(self):
        pass

    def elegir_kia(self):
        while True:
            print()
            print("Escoja el modelo de Kia que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehículo seleccionado Kia Forte")
            elif opcion == "2":
               print("Vehículo seleccionado Kia Optima")
            elif opcion == "3":
               print("Vehículo seleccionado Kia Seltos")
            elif opcion == "4":
               print("Vehículo seleccionado Kia Sportage")
            elif opcion == "5":
               print("Vehículo seleccionado Kia Sorento")
            elif opcion == "6":
               print("Vehículo seleccionado Kia Telluride")
            elif opcion == "7":
               print("Vehículo seleccionado Kia Rio")
            elif opcion == "8":
               print("Vehículo seleccionado Kia Soul")
            elif opcion == "9":
               print("Vehículo seleccionado Kia Carnival")
            elif opcion == "10":
               print("Vehículo seleccionado Kia Stinger")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
