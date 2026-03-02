class Masina:
    def __init__(self, marca, model, token, pret_ach, pret_vanz):
        self.marca = marca
        self.model = model
        self.token = token
        self.pret_ach = pret_ach
        self.pret_vanz = pret_vanz

    def __str__(self):
        return f"{self.marca} {self.model} {self.token} {self.pret_ach} {self.pret_vanz}"

def cmp_token(a, b):
    if a.token < b.token:
        return -1
    elif a.token > b.token:
        return 1
    else:
        return 0

def cmp_profit(a, b):
    profit_a = a.pret_vanz - a.pret_ach
    profit_b = b.pret_vanz - b.pret_ach

    if profit_a < profit_b:
        return -1
    elif profit_a > profit_b:
        return 1
    else:
        return 0

def sort(lista, comparator):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparator(lista[j], lista[j + 1]) > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

masini = [
    Masina("Audi", "A6", "x9f3a2", 5000, 9000),     # profit = 4000
    Masina("BMW", "X5", "a1b2c3", 8000, 12000),    # profit = 4000
    Masina("Ford", "Focus", "m7n8p9", 6000, 7500), # profit = 1500
    Masina("Toyota", "Corolla", "k4l5m6", 7000, 9500), # profit = 2500
    Masina("Volvo", "XC60", "b9a8c7", 9000, 15000),    # profit = 6000
    Masina("Audi", "A4", "z1y2x3", 4000, 7000)     # profit = 3000
]

print("Lista de masini sortata dupa token")
print("--------------------------------------")

masini_dupa_token = sort(masini, cmp_token)
for m in masini_dupa_token:
    print(m)
print("Lista de masini sortata dupa profit")
print("--------------------------------------")
masini_dupa_profit = sort(masini, cmp_profit)
for m in masini_dupa_profit:
    print(m)