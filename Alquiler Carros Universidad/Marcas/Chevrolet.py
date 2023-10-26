class Chevrolet:

    modelos_chevrolet = [
        "Chevrolet Malibu",
        "Chevrolet Impala",
        "Chevrolet Equinox",
        "Chevrolet Traverse",
        "Chevrolet Silverado",
        "Chevrolet Colorado",
        "Chevrolet Camaro",
        "Chevrolet Corvette",
        "Chevrolet Blazer",
        "Chevrolet Suburban",
        # Puedes añadir más modelos de Chevrolet aquí
    ]

    def __init__(self):
        pass

    def elegir_chevrolet(self):
        while True:
            print()
            print("Escoja el modelo de Chevrolet que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehículo seleccionado Chevrolet Malibu")
            elif opcion == "2":
               print("Vehículo seleccionado Chevrolet Impala")
            elif opcion == "3":
               print("Vehículo seleccionado Chevrolet Equinox")
            elif opcion == "4":
               print("Vehículo seleccionado Chevrolet Traverse")
            elif opcion == "5":
               print("Vehículo seleccionado Chevrolet Silverado")
            elif opcion == "6":
               print("Vehículo seleccionado Chevrolet Colorado")
            elif opcion == "7":
               print("Vehículo seleccionado Chevrolet Camaro")
            elif opcion == "8":
               print("Vehículo seleccionado Chevrolet Corvette")
            elif opcion == "9":
               print("Vehículo seleccionado Chevrolet Blazer")
            elif opcion == "10":
               print("Vehículo seleccionado Chevrolet Suburban")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
