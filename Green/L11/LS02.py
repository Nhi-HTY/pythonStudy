n = int(input())
a = list(map(int, input().split()))

def merge(nL, L, nR, R, array):
    i = j = k = 0
    while (i<nL and j < nR):
        if L[i] > R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while(i < nL):
        array[k] = L[i]
        k +=1
        i += 1
    while (j < nR):
        array[k] = R[j]
        k += 1
        j += 1

def mergeSort(array, n):
    if n>1:
        nL = n//2
        nR = n - nL

        L = array[:nL]
        R = array[nL:n]

        mergeSort(L, nL)
        mergeSort(R, nR)
        merge(nL, L, nR, R, array)

mergeSort(a, n)
for x in a:
    print(x, end=' ')
