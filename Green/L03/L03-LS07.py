a = int(input())

first = "*"*a
last = "*"*a

for i in range (0, a-2):
    middle = "*" + " "*(a-2) + "*" + "\n"

    middle_lines = (a-2)*middle
if a <=2:
    print ("{}\n{}".format(first, last))

else:
    print ("{}\n{}{}".format(first, middle_lines, last))
