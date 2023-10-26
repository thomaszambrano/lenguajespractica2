class Carro:
    def __init__(self, marca, modelo, año, numeroSerie, tarifa):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.numeroSerie = numeroSerie
        self.tarifa = tarifa

    @staticmethod
    def atributos(carro):
        info = ""
        info += "La marca del vehiculo es: {}\n".format(carro.marca)
        info += "El modelo del vehiculo es: {}\n".format(carro.edad)
        info += "El año del vehiculo es: {}\n".format(carro.año)
        info += "El numero de serie del vehiculo es: {}\n".format(carro.numeroSerie)
        info += "La tarifa del vehiculo es: {}\n".format(carro.tarifa)
        return info