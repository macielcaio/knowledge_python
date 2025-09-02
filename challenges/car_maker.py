from struct import pack_into


class Car:
    def __init__(self, make, model, year, color, fuel_level=100):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = fuel_level # Initial fuel level

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color}), Fuel: {self.fuel_level}%"

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")

def novo_carro():
    carro = Car("fiat", "toro", 2022, "black", 300)
    return carro

def novo_carro2():
    carro = Car("dodge", "ram", 2022, "black")
    return carro

print(novo_carro())
print(novo_carro2())