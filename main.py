class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    def acelerar(self):
        pass  # * Polimorfismo

    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")  # * Polimorfismo


class Auto(Vehiculo):  # * Herencia
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # * Herencia
        self.__puertas = puertas  # * Encapsulamiento

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def acelerar(self):  # * Polimorfismo
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está frenando.")  # * Polimorfismo


class Motocicleta(Vehiculo):  # * Herencia
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)  # * Herencia
        self.__cilindrada = cilindrada  # * Encapsulamiento

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def acelerar(self):  # * Polimorfismo
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} está frenando.")  # * Polimorfismo


class Camion(Vehiculo):  # * Herencia
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)  # * Herencia
        self.__capacidad_carga = capacidad_carga  # * Encapsulamiento

    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):  # * Polimorfismo
        print(f"El camion {self.get_marca()} {self.get_modelo()} con capacidad de carga {self.get_capacidad_carga()}kg está acelerando.")

    def detener(self):
        print(f"El camion {self.get_marca()} {self.get_modelo()} está frenando.")  # * Polimorfismo


if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "FH16": Camion("Volvo", "FH16", 2021, 25000)
    }

    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()
        vehiculo.detener()
