import random
from SDA.domain.entities import Car
from SDA.infrastructure.algorithms.sorting import sort_alg_type

def benchmark_sort(lista, sorting_function, original_comparator):
    contor = [0]

    def spy_comparator(a, b):
        contor[0] += 1  # Numărăm de cate ori s-a folosit operatia de comparare
        return original_comparator(a, b)  # Returnăm rezultatul real

    # Rulăm algoritmul pasându-i spy_comparator în loc de comparatorul original
    lista_sortata = sorting_function(lista, spy_comparator)

    return lista_sortata, contor[0]


def genereaza_masini_random(n):
    marci_modele = [("Audi", "A4"), ("BMW", "3Series"), ("Toyota", "Corolla"),
                    ("Ford", "Focus"), ("Volvo", "XC90"), ("Chevrolet", "Malibu")]
    lista = []
    for _ in range(n):
        marca, model = random.choice(marci_modele)
        token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        pret_ach = random.randint(1000, 10000)
        pret_vanz = pret_ach + random.randint(500, 5000)
        lista.append(Car(marca, model, token, pret_ach, pret_vanz))
    return lista


# 2. DATELE INIȚIALE (N=46)
date = """Chevrolet Malibu fuvjx4hgj4 4236 4199
Chevrolet Silverado wjckx944uj 7693 7494
Ford Transit iumj7qirqq 3214 9045
Volvo 850 bv55fq9ewq 2640 13400
Toyota LandCruiser fdm98gbg9j 3358 8395
Chevrolet Silverado3500HD 98kskdu1cr 1570 11285
Toyota T100 0yi1ocmlxn 4156 8313
Toyota Avalon x8fu5lo3m9 8920 3916
Audi A8 340fvt339e 4720 7764
Ford Taurus sqaybhpqj4 3013 13071
Audi S7 2qyapt359a 5705 3122
Audi RS5 nj3l315y1x 3254 11875
Chevrolet Cavalier h2uwk5jfev 8632 10334
Suzuki SX4 ikn8ntwin4 2036 6299
Ford Econoline d71a92ggfp 6788 12876
Mercedes-Benz Mercedes-AMG yx6196wdcm 5032 3670
Mercedes-Benz E-Class k6xeulilfw 5390 3272
BMW M5 lce7r3xqpr 6919 8237
BMW 1Series c36jtvjrcu 9557 11029
Toyota Tundra xx4e32mtje 4739 7576
Audi A6 amsbl4aixl 5463 8885
Chevrolet Express2500 etxita8lic 3976 11103
Chevrolet Malibu q2dip9g0uy 7012 5473
Toyota Highlander wll61s7abu 1278 7862
BMW X5 ndizj7lng2 2168 14999
Ford Taurus 1yklhcll8a 3515 9764
BMW 3Series 61lxnbay0c 6692 13222
Subaru Outback z3bohgt66y 5152 14411
Toyota RAV4 3n6wpwsbqk 6415 7899
Chevrolet 3500RegularCab ynyb4usatm 8344 10074
Suzuki Esteem qqdl4gg4r3 6926 10475
Ford Fiesta dwhod1a3w5 9995 8986
Toyota Mirai zn7jpf4dgp 5806 8925
Subaru BRZ 0ibdu3n47t 2987 3046
Chevrolet Silverado3500RegularCab di5qz4ctha 6154 9158
Ford F150SuperCrewCab btvw4mv2sp 2881 13344
Suzuki Sidekick 7s0t39eqv4 6138 9737
Audi A3 wt98fnpsku 3816 8993
Volvo V40 foi01znl24 6604 12283
Chevrolet Suburban ke07khg1wn 4121 4704
BMW 3Series 8gwhddclcg 2940 14865
BMW 5Series 8fpkfs7s9d 6058 13860
Chevrolet S10RegularCab ej39lnz1yx 1959 4909
Mercedes-Benz SLK-Class 4mq9w00wct 9604 4864
Mercedes-Benz CLK-Class paau62q56q 1477 2391
BMW 3Series b9cjvyigx8 2537 8550"""

lista_masini_initial = []
for line in date.split('\n'):
    arr = line.strip().split()
    if arr:
        lista_masini_initial.append(Car(arr[0], arr[1], arr[2], int(arr[3]), int(arr[4])))

comparatori = [
    ("Token", Car.cmp_token),
    ("Marca si Model", Car.cmp_marca_model),
    ("Marca, Model, Token", Car.cmp_marca_model_token),
    ("Profit", Car.cmp_profit)
]

dimensiuni_N = [len(lista_masini_initial), 100, 500, 1000, 5000]


print("\n" + "=" * 68)
print(f"{'STUDIU COMPARATIV: BUBBLE SORT vs MERGE SORT':^68}")
print("=" * 68)

for nume_cmp, comparator in comparatori:
    print(f"\n>>> Criteriu de sortare: {nume_cmp.upper()}")

    print(f"{'N (Dimensiune)':>15} | {'Bubble Sort O(n^2)':>22} | {'Merge Sort O(n log n)':>22}")
    print("-" * 68)

    for N in dimensiuni_N:
        if N == len(lista_masini_initial):
            lista_test = lista_masini_initial[:]
        else:
            lista_test = genereaza_masini_random(N)

        lista_bubble, op_bubble = benchmark_sort(
            lista_test,
            lambda lst, cmp: sort_alg_type(lst, cmp, alg="bubble"),
            comparator
        )

        lista_sort, op_merge = benchmark_sort(
            lista_test,
            lambda lst, cmp: sort_alg_type(lst, cmp, alg="merge"),
            comparator
        )

        print(f"{N:>15} | {op_bubble:>22} | {op_merge:>22}")

print("\n" + "=" * 68 + "\n")