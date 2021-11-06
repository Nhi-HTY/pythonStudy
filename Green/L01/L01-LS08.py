basic_salary = int(input())
coefficient = float(input())
allowance = int(input())

salary = basic_salary*coefficient + allowance
print ("{:.2f}".format(salary))