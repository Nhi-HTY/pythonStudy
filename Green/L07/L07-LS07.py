inputString = input()

ans = ""
doUpperCase = False

j=0
while(j< len(inputString)):
    if doUpperCase == True and inputString[j] != " ":
        ans += inputString[j].upper()
        doUpperCase = False
        j +=1
    elif j+1 < len(inputString):
        if inputString[j] == "." and inputString[j+1] == " ":
            ans += inputString[j]
            ans += inputString[j+1]
            doUpperCase = True
            j +=2
        else:
            ans +=inputString[j]
            j +=1
    else:
        ans += inputString[j]
        j += 1
print(ans)