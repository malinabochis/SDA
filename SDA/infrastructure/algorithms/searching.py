def sequential_search(arr, target, comparator):
    for elem in arr:
        if comparator(elem, target) == 0: # comparatorul returnează 0 dacă obiectele sunt "egale" conform criteriului
            return elem
    return None

def binary_search(arr, target, comparator):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        cmp = comparator(arr[mid], target)
        if cmp == 0:
            return arr[mid]
        elif cmp < 0:
            left = mid + 1
        else:
            right = mid - 1
    return None

def search_alg_type(arr, target, comparator, alg = "sequential"):
    if alg == "sequential":
        return sequential_search(arr, target, comparator)
    elif alg == "binary":
        return binary_search(arr, target, comparator)
    else:
        raise ValueError("Algoritm de cautare necunoscut")