t =int(input())

def transform(expression):
    s = []
    for i in range(len(expression)):
        if expression[i] == "(":
            i += 1
        elif expression[i].isalpha():
            print(expression[i], end="")
        elif expression[i] == ")":
            print(s.pop(), end = "")
        else:
            s.append(expression[i])
    print()

for i in range(t):
    expression = input()
    transform(expression)


