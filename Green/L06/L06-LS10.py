row, column = map(int, input().split())

a, b, p = map(int, input().split())

array = []
matrix =[]

array.append(a)
array.append(b)

size = row * column

for i in range(2, size):
    result = (array[i-1]+ array[i-2]) % p
    array.append(result)

tmp = column
i =0
while(tmp<=size):
    matrix.append(array[i:tmp])
    i = tmp
    tmp += column

for k in range(len(matrix)):
    for l in range(len(matrix[k])):
        print(matrix[k][l], end= " ")
    print("")
