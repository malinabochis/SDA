class CarRepositoryException(Exception):
    pass


class CarRepository:
    def __init__(self, validator):
        self.__all_cars = {}
        self.__validator = validator

    def save(self, car):
        self.__validator.validate(car)
        if self.find_by_token(car.token) is not None:
            raise CarRepositoryException(f"Car with token {car.token} already exists")
        self.__all_cars[car.token] = car

    def find_all(self):
        return list(self.__all_cars.values())

    def update(self, car):
        if self.find_by_token(car.token) is None:
            raise CarRepositoryException("Car token does not exist")
        self.__all_cars[car.token] = car

    def delete_by_token(self, token):
        if self.find_by_token(token) is None:
            raise CarRepositoryException("Car token does not exist")
        del self.__all_cars[token]

    def find_by_token(self, token):
        return self.__all_cars.get(token, None)