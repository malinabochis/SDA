from SDA.domain.entities import Car
from SDA.repository.car_repository import CarRepository
class CarFileRepository(CarRepository):
    def __init__(self, car_validator, file_name):
        super().__init__(car_validator)
        self.__file_name = file_name
        self.__load_data()

    # =========================
    # INCARCARE DIN FISIER
    # =========================
    def __load_data(self):
        try:
            with open(self.__file_name, "r") as f:
                for line in f:
                    line = line.strip()
                    if line != "":
                        data = line.split(",")

                        marca = data[0]
                        model = data[1]
                        token = data[2]
                        pret_ach = int(data[3])
                        pret_vanz = int(data[4])

                        car = car(marca, model, token, pret_ach, pret_vanz)
                        self.__all_cars.append(car)

        except FileNotFoundError:
            print("Fisierul nu exista. Se va crea automat la prima salvare.")

    # =========================
    # GET ALL (copie!)
    # =========================
    def get_all_cars(self):
        return self.__all_cars[:]

    # =========================
    # SAVE (memorie + fisier)
    # =========================
    def save(self, car):
        # salvam in memorie
        self.__all_cars.append(car)

        # salvam si in fisier
        with open(self.__file_name, "a") as f:
            f.write(f"{car.marca},{car.model},{car.token},{car.pret_ach},{car.pret_vanz}\n")