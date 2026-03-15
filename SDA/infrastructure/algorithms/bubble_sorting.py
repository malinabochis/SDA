"""BUBBLE SORT --> COMPLEXITATE: n^2"""


def sort_bubble_cars(self, comparator):
    """
    Sortare generică folosind Bubble Sort.
    :param comparator: o funcție care primește două obiecte și returnează 1 pentru swap.
    """
    cars = self.__repository.get_all_cars()
    n = len(cars)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Apelăm comparatorul generic primit ca parametru
            if comparator(cars[j], cars[j + 1]) > 0:
                cars[j], cars[j + 1] = cars[j + 1], cars[j]
    return cars