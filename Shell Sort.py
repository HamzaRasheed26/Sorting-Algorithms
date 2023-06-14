def shellSort(array, n, order):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            if order == "Asc":
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
            elif order == "Des":
                while j >= interval and array[j - interval] < temp:
                    array[j] = array[j - interval]
                    j -= interval

            array[j] = temp
        interval //= 2

import random
def RandomArray(size):
    arr = []
    for i in range(size):
        num = random.randint(0, 100)
        arr.append(num)
    return arr


arr = RandomArray(20)
print(arr)

shellSort(arr, 20, "Asc")
print(arr)
