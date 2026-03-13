from SDA.domain.entities import Car
from SDA.infrastructure.algorithms.sorting import merge, merge_sort, sort_alg_type


class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def find_by_token(self, token):
        return self.__car_repository.find_by_token(token)

    def add_car(self, marca, model, token, pret_ach, pret_vanz):
        car = Car(marca, model, token, pret_ach, pret_vanz)
        self.__car_repository.save(car)

    def get_all_cars(self):
        return self.__car_repository.find_all()

    def cmp_profit(self, a, b):
        profit_a = a.pret_vanz - a.pret_ach
        profit_b = b.pret_vanz - b.pret_ach

        if profit_a < profit_b:
            return -1
        elif profit_a > profit_b:
            return 1
        else:
            return 0

    def sort_cars(self, cmp):
        lista_masini = self.get_all_cars()
        return sort_alg_type(lista_masini, cmp)

    def sort_secondary(self, i1, j1, criteriu):
        cars = self.__repository.get_all_cars()

        if criteriu == "profit":
            profit_i = cars[i1].pretVanzare - cars[i1].pretAchizitie
            profit_j = cars[j1].pretVanzare - cars[j1].pretAchizitie

            if profit_i > profit_j:
                cars[i1], cars[j1] = cars[j1], cars[i1]
                return 1
            return 0

        else:
            key = lambda obj: getattr(obj, criteriu)

            if key(cars[i1]) > key(cars[j1]):
                cars[i1], cars[j1] = cars[j1], cars[i1]
                return 1

        return 0

def sort_all_cars(self, criterii):  # BubbleSort - avand ordin de complexitate O(n^2)
    cars = self.__repository.get_all_cars()
    n = len(cars)
    n1 = len(criterii)
    ok = 0
    if criterii[0] == "profit":
        key1 = lambda obj: getattr(obj, "pretAchizitie")
        key2 = lambda obj: getattr(obj, "pretVanzare")

    else:
        key = lambda obj: getattr(obj, criterii[0])
    for i in range(n):
        for j in range(0, n - i - 1):
            if criterii[0] == "profit":
                cond = (key2(cars[j]) - key1(cars[j])) > (key2(cars[j + 1]) - key1(cars[j + 1]))
                cond1 = (key2(cars[j]) - key1(cars[j])) == (key2(cars[j + 1]) - key1(cars[j + 1]))
                if cond == True:
                    cars[j], cars[j + 1] = cars[j + 1], cars[j]
            else:
                if key(cars[j]) > key(cars[j + 1]):
                    cars[j], cars[j + 1] = cars[j + 1], cars[j]
                if key(cars[j]) == key(cars[j + 1]) and len(criterii) > 1:
                    for k in range(1, n1):
                        valoare = self.sort_secondary(j, j + 1, criterii[k])
                        if valoare == 1:
                            break
    return cars


def search(self, valoare):
    cars = self.__repository.get_all_cars()
    criterii = ["marca", "model", "token", "pretAchizitie", "pretVanzare"]

    results = []

    for criteriu in criterii:
        for car in cars:
            if getattr(car, criteriu) == valoare:
                results.append(car)

    return results