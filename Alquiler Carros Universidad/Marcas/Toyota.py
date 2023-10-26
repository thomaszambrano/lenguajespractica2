class Toyota:

    modelos_toyota = [
        "Toyota Corolla",
        "Toyota Camry",
        "Toyota RAV4",
        "Toyota Highlander",
        "Toyota Tacoma",
        "Toyota Prius",
        "Toyota 4Runner",
        "Toyota Sienna",
        "Toyota Tundra",
        "Toyota C-HR",
        # Puedes añadir más modelos de Toyota aquí
    ]

    def __init__(self):
        pass

    def elegir_toyota(self):
        while True:
            print()
            print("Escoja el modelo de Toyota que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehículo seleccionado Toyota Corolla")
            elif opcion == "2":
               print("Vehículo seleccionado Toyota Camry")
            elif opcion == "3":
               print("Vehículo seleccionado Toyota RAV4")
            elif opcion == "4":
               print("Vehículo seleccionado Toyota Highlander")
            elif opcion == "5":
               print("Vehículo seleccionado Toyota Tacoma")
            elif opcion == "6":
               print("Vehículo seleccionado Toyota Prius")
            elif opcion == "7":
               print("Vehículo seleccionado Toyota 4Runner")
            elif opcion == "8":
               print("Vehículo seleccionado Toyota Sienna")
            elif opcion == "9":
               print("Vehículo seleccionado Toyota Tundra")
            elif opcion == "10":
               print("Vehículo seleccionado Toyota C-HR")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
