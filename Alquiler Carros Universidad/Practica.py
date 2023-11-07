def controlador():
    print("Bienvenido al software de alquiler de vehiculos")
    mostrar_menu()


def mostrar_menu():
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


def menu_alquilar_carro():
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


def menu_carros_alquilados():
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


def imprimirListas(modelo_a_buscar):
    for lista_de_modelo in lista_de_modelos:
        if modelo_a_buscar in lista_de_modelo:
            print(modelo_a_buscar)
            break


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

lista_de_modelos = [
    modelos_chevrolet,
    modelos_kia,
    modelos_mazda,
    modelos_renault,
    modelos_toyota,
    modelos_volkswagen
]
controlador()
