class Employee():
    def __init__(self, listEmployee):
        self.list = listEmployee

    def countAge(self):
        maxAge = int(self.list[0][2])
        maxEmployee = self.list[0]
        for row in range(len(self.list)):
            if int(self.list[row][2]) < maxAge:
                maxAge = int(self.list[row][2])
                maxEmployee = self.list[row]
            else:
                if int(self.list[row][2]) == maxAge:
                    if int(self.list[row][0]) < int(maxEmployee[0]):
                        maxEmployee = self.list[row]
        return  maxEmployee
n = int(input())
listEmployee = []

for i in range(0, n):
    employee = list(map(str, input().split()))
    listEmployee.append(employee)

result = Employee(listEmployee).countAge()

for x in result:
    print(x, end = " ")