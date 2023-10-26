from Carro import Carro

class Renta(Carro):
    def __init__(self, marca, modelo, año, numeroSerie, tarifa):
       super().__init__(marca, modelo, año, numeroSerie, tarifa)
    

    def alquilar_carro(self):
         while True:
            print()
            print("Lista de marcas disponibles para el alquiler")
            print()
            print("1. Chevrolet")
            print("2. Renault")
            print("3. Volkswagen")
            print("4. Toyota")
            print("5. Kia")
            print("6. Mazda")
            print("7. Volver al menú principal")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               print("Lista de vehiculos Chevrolet")
            elif opcion == "2":
               print("Lista de vehiculos renault")
            elif opcion == "3":
               print("Lista de vehiculos Volkswagen")
            elif opcion == "4":
               print("Lista de vehiculos Toyota")
            elif opcion == "5":
               print("Lista de vehiculos Kia")  
            elif opcion == "6":
               print("Lista de vehiculos Mazda")  
            elif opcion == "7":
                print("--------------------------------------------------------")
                print("Ha regresado al menú principal")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")