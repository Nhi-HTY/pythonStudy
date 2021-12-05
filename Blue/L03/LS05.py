people, bottleLitter = map(int, input().split())
listCup = list(map(int, input().split()))

listCup.sort(reverse=True)
maxLitter = 0
i = 0
maleLitter = listCup[i+people-1] * people
femaleLitter = maleLitter/2
maxFemaleLitter = listCup[len(listCup)-1] * people
while femaleLitter > maxFemaleLitter:
    maleLitter = listCup[i + people - 1] /2 * people
    femaleLitter = maleLitter / 2
else:
    maxLitter = maleLitter + femaleLitter + 0.0
if maxLitter > bottleLitter:
    maxLitter = bottleLitter + 0.0

print(int(maxLitter)) if maxLitter.is_integer() else print(maxLitter)


