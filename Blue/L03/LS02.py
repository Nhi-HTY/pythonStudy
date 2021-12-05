totalChores, petyaChores, vasyaChores = map(int, input().split())
listChores = list(map(int, input().split()))

listChores.sort()

smallestPetyaChore = listChores[vasyaChores]
largestVasyaChore = listChores[vasyaChores-1]
ans = smallestPetyaChore - largestVasyaChore
print(ans)