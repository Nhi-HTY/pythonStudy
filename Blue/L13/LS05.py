n = int(input())
listPenguin = {"Emperor": 0, "Macaroni": 0, "Little": 0}
for _ in range(n):
    penguin = input()
    if penguin.__contains__("Emperor"):
        listPenguin["Emperor"] += 1
    elif penguin.__contains__("Macaroni"):
        listPenguin["Macaroni"] += 1
    else:
        listPenguin["Little"] += 1

max = 0
maxName = ""
for penguin in listPenguin:
    if listPenguin[penguin] > max:
        max = listPenguin[penguin]
        maxName = penguin

print("{} Penguin".format(maxName))