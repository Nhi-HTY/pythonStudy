bag1, bag2, bag3, bag4 = map(int, raw_input().split())

if (bag1 > bag2 and bag1 > bag3 and bag1 > bag4):
    max = bag1
    print (max)
elif (bag2 > bag1 and bag2 > bag3 and bag2 > bag4):
    max = bag2
    print (max)
elif (bag3 > bag1 and bag3 > bag2 and bag3 > bag4):
    max = bag3
    print (max)
else:
    max = bag4
    print (max)

