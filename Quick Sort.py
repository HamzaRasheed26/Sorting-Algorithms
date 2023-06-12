import random


def partition(array, low, high, mode):
    pivot = array[high]

    i = low - 1
    if mode == "Asc":
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])

    if mode == "Des":
        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high, mode):
    if low < high:
        pi = partition(array, low, high, mode)

        quickSort(array, low, pi - 1, mode)

        quickSort(array, pi + 1, high, mode)

# function for generating array of random numbers


def RandomArray(size):
    arr = []
    for i in range(size):
        num = random.randint(0, 100)
        arr.append(num)
    return arr


arr = RandomArray(20)
print(arr)

quickSort(arr, 0, 19, "Asc")
print(arr)
