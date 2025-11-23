class Carro:
    def __init__(self, marca, modelo, ano, cor="Branco", motor="1.0", opcionais=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.opcionais = opcionais or []

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} - {self.cor}, motor {self.motor}, opcionais: {self.opcionais}"



carro1 = Carro("Ford", "Fiesta", 2020, "Preto", "1.6", ["Ar", "ABS", "Airbag"])

print(carro1)
