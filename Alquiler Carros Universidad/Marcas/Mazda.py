class Mazda:


    modelos_mazda = [
        "Mazda3",
        "Mazda6",
        "Mazda CX-3",
        "Mazda CX-5",
        "Mazda CX-9",
        "Mazda MX-5 Miata",
        "Mazda MX-30 (eléctrico)",
        "Mazda RX-8 (modelo anterior)",
        "Mazda5 (modelo anterior)",
        "Mazda Tribute (modelo anterior)"
    ]

    
    def __init__(self) -> None:
        pass

    def elegir_mazda(self):
        while True:
            print()
            print("Escoga el modelo de Mazda que desea alquilar: ")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Vehiculo seleccionado Mazda3")
            elif opcion == "2":
               print("Vehiculo seleccionado Mazda6")
            elif opcion == "3":
               print("Vehiculo seleccionado Mazda CX-3")
            elif opcion == "4":
               print("Vehiculo seleccionado Mazda CX-5")
            elif opcion == "5":
               print("Vehiculo seleccionado Mazda CX-9")
            elif opcion == "6":
               print("Vehiculo seleccionado Mazda MX-5 Miata")
            elif opcion == "7":
               print("Vehiculo seleccionado Mazda MX-30 (eléctrico)")
            elif opcion == "8":
               print("Vehiculo seleccionado Mazda RX-8")
            elif opcion == "9":
               print("Vehiculo seleccionado Mazda5")
            elif opcion == "10":
               print("Vehiculo seleccionado Mazda Tribute")
            elif opcion == "11":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")