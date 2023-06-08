# function for merging array using merge algorithm
def Merge(A, p, q, r):
    n1 = q-p + 1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    if type(A[0]) == int:
        L[n1] = 99999999
        R[n2] = 99999999
    else:
        L[n1] = "zzzzzzzzzzzzzzz"
        R[n2] = "zzzzzzzzzzzzzzz"
    i = 0
    j = 0
    k = p
    while k <= r:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

# function for sorting array using merge sorting algorithm


def MergeSort(A, p, r):
    if p < r:
        q = int((p+r)/2)

        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)
