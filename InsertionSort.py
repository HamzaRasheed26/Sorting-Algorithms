# function for sorting array using insertion sorting algorithm
def InsertionSort(array, start, end):
    for i in range(start+1,end+1):
        key = array[i]
        x = i-1
        while key < array[x] and x >= 0:
            array[x+1] = array[x]
            x = x -1 
        array[x+1] = key
    return array