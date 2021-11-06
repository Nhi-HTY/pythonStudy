last, current = map(float, raw_input().split())

used = current - last

if (0 < used <=50):
    pay = (used*1484 + used*1484*0.1)
    print (int(pay))
elif (51 <= used <=100):
    pay = 50*1484 + (used - 50)*1533
    print (int(pay + pay*0.1))
elif(101 <= used <=200):
    pay = (50 * 1484 + 50*1533) + (used - 100)*1786
    print (int(pay + pay*0.1))
elif(201 <= used <=300):
    pay = (50 * 1484 + 50*1533 + 100*1786) + (used - 200)*2242
    print (int(pay + pay*0.1))
elif (301 <= used <= 400):
    pay = (50 * 1484 + 50 * 1533 + 100 * 1786 + 100*2242) + (used - 300) * 2503
    print (int(pay + pay*0.1))
elif (401 <= used):
    pay = (50 * 1484 + 50 * 1533 + 100 * 1786 + 100*2242 + 100*2503) + (used - 400) * 2587
    print (int(pay + pay*0.1))