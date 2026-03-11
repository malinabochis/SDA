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