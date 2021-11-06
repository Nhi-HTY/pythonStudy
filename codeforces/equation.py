def remove_zero(a, b):
    result = a + b
    first_number =0
    result_a = []
    str_a = str(a)
    length_a = len(str(a)[::-1])
    for i in range(length_a):
        n = str_a[i]
        if n != str(0):
            result_a += n

remove_zero(203, 3)