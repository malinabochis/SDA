class Car:
    def __init__(self, marca, model, token, pret_ach, pret_vanz):
        self.marca = marca
        self.model = model
        self.token = token
        self.pret_ach = pret_ach
        self.pret_vanz = pret_vanz

    def __str__(self):
        return f"{self.marca} {self.model} {self.token} {self.pret_ach} {self.pret_vanz}"