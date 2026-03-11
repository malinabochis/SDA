from SDA.domain.validators import CarValidator
from SDA.repository.file_repository import CarFileRepository
from SDA.service.car_service import CarService
from SDA.ui.console import AppConsole


def main():
    car_validator = CarValidator()
    car_repository = CarFileRepository(car_validator, "../data/cars")
    car_service = CarService(car_repository)
    app_console = AppConsole(car_service)
    app_console.run_console()

main()