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

def merge_sort(arr, left, right, comparator):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, comparator)
        merge_sort(arr, mid + 1, right, comparator)
        merge(arr, left, mid, right, comparator)
    return arr

def sort_alg_type(lista, comparator):
    arr = lista[:] # copie dupa lista, ca sa nu se modifice ea insasi
    merge_sort(arr, 0, len(arr) - 1, comparator)
    return arr