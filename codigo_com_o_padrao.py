class Carro:
    def __init__(self, marca, modelo, ano, cor, motor, opcionais):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.opcionais = opcionais

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} - {self.cor}, motor {self.motor}, opcionais: {self.opcionais}"


class CarroBuilder:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.ano = None
        self.cor = "Branco"
        self.motor = "1.0"
        self.opcionais = []

    def set_marca(self, marca):
        self.marca = marca
        return self

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self

    def set_ano(self, ano):
        self.ano = ano
        return self

    def set_cor(self, cor):
        self.cor = cor
        return self

    def set_motor(self, motor):
        self.motor = motor
        return self

    def add_opcional(self, opcional):
        self.opcionais.append(opcional)
        return self

    def build(self):
        return Carro(
            self.marca, self.modelo, self.ano,
            self.cor, self.motor, self.opcionais
        )



carro2 = (
    CarroBuilder()
    .set_marca("Ford")
    .set_modelo("Fiesta")
    .set_ano(2020)
    .set_cor("Preto")
    .set_motor("1.6")
    .add_opcional("Ar")
    .add_opcional("ABS")
    .add_opcional("Airbag")
    .build()
)

print(carro2)
