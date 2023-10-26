from Controlador import Controlador

class Main:
    def __init__(self):
        print()
        print("Bienvenido al software de Alquiler de vehiculos")
        print()
        self.controlador = Controlador()
    #La main ejecuta el programa llamando a controlador
    def main(self):
        self.controlador.controlar()


if __name__ == "__main__":
    programa = Main()
    programa.main()