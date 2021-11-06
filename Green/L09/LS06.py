import sys
sys.setrecursionlimit(10000)
n = int(input())

array = list(map(int, input().split()))
rest = []

def countEvent(array):
    evenNumber = 0
    last = array[len(array)-1]
    array.pop(len(array)-1)
    if last %2 == 0:
        evenNumber = last
    if len(array) > 0:
        return evenNumber + countEvent(array)
    else:
        return evenNumber


print(countEvent(array))