class Student():
    def __init__(self, grade):
        self.g = grade

    def countGPA(self):
        count = 0
        for row in range(len(self.g)):
            GPA = (self.g[row][0] + self.g[row][1])/2
            if GPA>=9.0:
                count +=1
        return count

n = int(input())

studentGrade = []

for i in range(0, n):
    name = input()
    grade = list(map(float, input().split()))
    studentGrade.append(grade)

count = Student(studentGrade).countGPA()

print(count)