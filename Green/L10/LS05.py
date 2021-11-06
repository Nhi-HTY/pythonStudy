n, q = map(int, input().split())

class Student():
    def __init__(self, listStudent, queries):
        self.list = listStudent
        self.q = queries

    def searchStudent(self):
        result = []
        for i in range(len(self.q)):
            eachStudentScore = []
            for row in range(len(self.list)):
                if self.q[i] == self.list[row][0]:
                    eachStudentScore.append(self.list[row][1])
                    eachStudentScore.append(self.list[row][2])
                    result.append(eachStudentScore)
        return result

listStudent = []
queries = []
for i in range(0, n):
    studentScore = list(map(float, input().split()))
    listStudent.append(studentScore)

for j in range(0, q):
    query = int(input())
    queries.append(query)

result = Student(listStudent, queries).searchStudent()
for row in range(len(result)):
    for col in range(0, 2):
        print(result[row][col], end = " ")
    print()