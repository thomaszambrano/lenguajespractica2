from Procesos.Rentar import Renta
from Procesos.Alquilados import Alquilados
Rentar = Renta(marca=None, modelo=None, año=None, numeroSerie=None, tarifa=None)
Alquilar = Alquilados()
class Menu:
    def __init__(self) -> None:
        pass
    # Mostrar_menu es uno de los metodos más importantes ya que acá estaran todas las decisiones del usuario
    def mostrar_menu(self):
        while True:
            print()
            print("1. Ver autos disponibles para alquiler")
            print("2. Hacer devolución de un vehiculo para el alquiler")
            print("3. Salir")
            print()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
               pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                print("--------------------------------------------------------")
                print("Se ha cerrado el software de alquiler de vehiculos")
                print()
                break
            else:
                print("Opción no válida. Intente de nuevo.")