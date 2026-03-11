from SDA.domain.entities import Car
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class AppConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def run_console(self):
        clear_screen()
        while True:
            self.__show_menu()
            cmd = input("> ").strip()

            if cmd.upper() == "EXIT":
                print("Iesire...")
                break

            try:
                self.__process_command(cmd)
            except Exception as e:
                print(f"Eroare: {e}")

            input("\nApasa ENTER pentru a reveni la meniu...")

    def __show_menu(self):
        print("\n=== Car Management Console ===")
        print("Comenzi disponibile:")
        print("  SEARCH tokenMasina")
        print("  SORT tokenMasina")
        print("  SORT marca model")
        print("  SORT marca model tokenMasina")
        print("  SORT profit")
        print("  EXIT\n")

    def __process_command(self, cmd):
        parts = cmd.split()

        if len(parts) == 0:
            print("Comanda invalida")
            return

        # SEARCH
        if parts[0].upper() == "SEARCH":
            if len(parts) != 2:
                print("Format corect: SEARCH tokenMasina")
                return
            self.__search(parts[1])
            return

        # SORT
        if parts[0].upper() == "SORT":
            self.__sort(parts[1:])
            return

        print("Comanda necunoscuta")

    # ---------------- SEARCH ----------------

    def __search(self, token):
        car = self.__car_service.find_by_token(token)
        if car is None:
            print("Masina nu exista.")
        else:
            print(car)

    # ---------------- SORT ----------------

    def __sort(self, args):

        # Alegem comparatorul din Car sau din Service
        if args == ["tokenMasina"]:
            cmp = Car.cmp_token

        elif args == ["marca", "model"]:
            cmp = Car.cmp_marca_model

        elif args == ["marca", "model", "tokenMasina"]:
            cmp = Car.cmp_marca_model_token

        elif args == ["profit"]:
            cmp = self.__car_service.cmp_profit

        else:
            print("Criteriu de sortare invalid.")
            return

        lista_sortata = self.__car_service.sort_cars(cmp)

        for car in lista_sortata:
            print(car)