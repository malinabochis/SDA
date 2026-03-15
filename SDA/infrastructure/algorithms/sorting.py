"""MERGE SORT --> COMPLEXITATE: n*log(n)"""

def merge(arr, left, mid, right, comparator):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if comparator(L[i], R[j]) <= 0: # comparatorul scris generic de mine va decide modul in care sunt sortate
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# def merge_sort(arr, left, right, comparator):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(arr, left, mid, comparator)
#         merge_sort(arr, mid + 1, right, comparator)
#         merge(arr, left, mid, right, comparator)
#     return arr


def merge_sort(arr, comparator):
    arr = arr[:]

    def _sort(left, right):
        if left < right:
            mid = (left + right) // 2

            _sort(left, mid)  # Sortăm jumătatea stângă
            _sort(mid + 1, right)  # Sortăm jumătatea dreaptă

            merge(arr, left, mid, right, comparator)

    if len(arr) > 1:
        _sort(0, len(arr) - 1)

    return arr


"""BUBBLE SORT --> COMPLEXITATE: n^2"""

def bubble_sort(arr, comparator):
    arr = arr[:]  # facem o copie ca să nu modificăm lista originală
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if comparator(arr[j], arr[j + 1]) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def sort_alg_type(lista, comparator, alg="merge"):
    if alg == "merge":
        return merge_sort(lista, comparator)
    elif alg == "bubble":
        return bubble_sort(lista, comparator)
    else:
        raise ValueError("Algoritm necunoscut")