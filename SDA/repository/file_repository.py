from SDA.domain.entities import Car
from SDA.repository.car_repository import CarRepository


class CarFileRepository(CarRepository):
    def __init__(self, car_validator, file_name):
        super().__init__(car_validator)
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                array = line.strip().split()   #strip() curata spatiile, tab urile si \n de la inceputul si sfarsitul liniei
                car = Car(array[0], array[1], array[2], int(array[3]), int(array[4]))
                super().save(car)

    def save(self, car):
        with open(self.__file_name, "a") as f:
            f.write(f"\n{car.marca},{car.model},{car.token},{car.pret_ach},{car.pret_vanz}")
        super().save(car)