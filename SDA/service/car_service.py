from SDA.domain.entities import Car
from SDA.infrastructure.algorithms.bubble_sorting import sort_bubble_cars
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

    # def sort_secventival(self, i1, j1, criteriu):
    #     cars = self.__repository.get_all_cars()
    #
    #     if criteriu == "profit":
    #         profit_i = cars[i1].pretVanzare - cars[i1].pretAchizitie
    #         profit_j = cars[j1].pretVanzare - cars[j1].pretAchizitie
    #
    #         if profit_i > profit_j:
    #             cars[i1], cars[j1] = cars[j1], cars[i1]
    #             return 1
    #         return 0
    #
    #     else:
    #         key = lambda obj: getattr(obj, criteriu)
    #
    #         if key(cars[i1]) > key(cars[j1]):
    #             cars[i1], cars[j1] = cars[j1], cars[i1]
    #             return 1
    #
    #     return 0

def sort_all_cars(self, cmp):  # BubbleSort - avand ordin de complexitate O(n^2)
    lista_masini = self.get_all_cars()
    return sort_bubble_cars(lista_masini, cmp)



def cauta_secventiala(self, criteriu_valoare, comparator):
    cars = self.__repository.get_all_cars()
    for car in cars:
        # comparatorul returnează 0 dacă obiectele sunt "egale" conform criteriului
        if comparator(car, criteriu_valoare) == 0:
            return car
    return None