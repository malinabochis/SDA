class Car:
    def __init__(self, marca, model, token, pret_ach, pret_vanz):
        self.marca = marca
        self.model = model
        self.token = token
        self.pret_ach = pret_ach
        self.pret_vanz = pret_vanz

    def __str__(self):
        return f"{self.marca} {self.model} {self.token} {self.pret_ach} {self.pret_vanz}"

    @staticmethod
    def cmp_token(a, b):
        if a.token < b.token:
            return -1
        elif a.token > b.token:
            return 1
        else:
            return 0

    @staticmethod
    def cmp_marca_model(a, b):
        if a.marca < b.marca:
            return -1
        elif a.marca > b.marca:
            return 1
        else:
            if a.model < b.model:
                return -1
            elif a.model > b.model:
                return 1
            else:
                return 0

    @staticmethod
    def cmp_marca_model_token(a, b):
        if a.marca < b.marca:
            return -1
        elif a.marca > b.marca:
            return 1
        else:
            if a.model < b.model:
                return -1
            elif a.model > b.model:
                return 1
            else:
                if a.token < b.token:
                    return -1
                elif a.token > b.token:
                    return 1
                else:
                    return 0

    @staticmethod
    def cmp_profit(a, b):
        profit_a = a.pret_vanz - a.pret_ach
        profit_b = b.pret_vanz - b.pret_ach

        if profit_a < profit_b:
            return -1
        elif profit_a > profit_b:
            return 1
        else:
            return 0