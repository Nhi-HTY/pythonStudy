birth_year = int(input())

if birth_year not in range(0,2019):
	print("enter a valid number between 0 and 2019")
else:
	age = 2019 - birth_year
	print(age)
