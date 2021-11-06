def insertDesc(a, i, x):
    j = i
    while(j>0):
        if a[j-1] >=x:
            break
        a[j] = a[j-1]
        j -=1
    a[j] = x

def insertAsc(a, i, x):
    j = i
    while(j>0):
        if a[j-1] <=x:
            break
        a[j] = a[j-1]
        j -=1
    a[j] = x

def insertSortAsc(a):
    for i in range(1, len(a)):
        x = a[i]
        insertAsc(a, i, x)

def insertSortDesc(a):
    for i in range(1, len(a)):
        x = a[i]
        insertDesc(a, i, x)

n, k = list(map(int, input().split()))
grade = []
listStudent = []

i =0
while i < n:
    x = list(map(float, input().split()))
    student = []
    grade.append(x[1])
    student.append(x[0])
    student.append(x[1])
    listStudent.append(student)
    i +=1

insertSortDesc(grade)

j=0
while j < k:
    code = []
    for row in range(len(listStudent)):
        if grade[j] == listStudent[row][1]:
            code.append(listStudent[row][0])
    if len(code) > 1:
        insertSortAsc(code)
        if (j < k-1):
            print(int(code[0]))
            print(int(code[1]))
            j+=1
        else:
            print(int(code[0]))
    else:
        print(int(code[0]))
    j +=1
