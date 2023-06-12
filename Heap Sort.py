import random


def heapify(arr, N, i, order):
    largest = i
    l = 2 * i
    r = 2 * i + 1

    if order == "Asc":
        if l < N and arr[largest] < arr[l]:
            largest = l

        if r < N and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            heapify(arr, N, largest, order)
    elif order == "Des":
        if l < N and arr[largest] > arr[l]:
            largest = l

        if r < N and arr[largest] > arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            heapify(arr, N, largest, order)


def BuildMaxHeap(arr, order):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i, order)


def HeapSort(array, order):
    BuildMaxHeap(array, order)
    N = len(array)

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0, order)

    return array


def RandomArray(size):
    arr = []
    for i in range(size):
        num = random.randint(0, 100)
        arr.append(num)
    return arr


arr = RandomArray(20)
print(arr)

HeapSort(arr, "Des")
print(arr)
