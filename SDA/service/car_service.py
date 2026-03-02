from SDA.domain.entities import Car


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