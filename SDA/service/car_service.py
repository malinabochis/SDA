from SDA.domain.entities import Car
from SDA.infrastructure.algorithms.searching import search_alg_type
from SDA.infrastructure.algorithms.sorting import merge, merge_sort, sort_alg_type


class CarService:
    def __init__(self, car_repository):
        self.__car_repository = car_repository

    def add_car(self, marca, model, token, pret_ach, pret_vanz):
        car = Car(marca, model, token, pret_ach, pret_vanz)
        self.__car_repository.save(car)

    def get_all_cars(self):
        return self.__car_repository.find_all()

    def sort_cars(self, cmp, alg = "merge"):
        lista_masini = self.get_all_cars()
        return sort_alg_type(lista_masini, cmp, alg)

    def search_car(self, target_car, comparator, alg="sequential"):
        lista_masini = self.get_all_cars()

        if alg == "binary":
            lista_masini = self.sort_cars(comparator, alg="merge") # Căutarea binară necesită un sistem perfect ordonat

        return search_alg_type(lista_masini, target_car, comparator, alg)