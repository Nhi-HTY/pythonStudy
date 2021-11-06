n = int(input())

def divisor(n):
    print('Input: ' + str(n))
    if n % 2 != 0:
        return n
    else:
        print('Khong chia het: ' + str(n))
        return divisor(n/2)
print(int(divisor(n)))