listVehicles = []
for i in range(4):
    vehicle = list(map(int, input().split()))
    listVehicles.append(vehicle)

flag = True
# check l
if listVehicles[0][0] == listVehicles[3][3] == 1:
    flag = False
if listVehicles[1][0] == listVehicles[0][3] == 1:
    flag = False
if listVehicles[2][0] == listVehicles[1][3] == 1:
    flag = False
if listVehicles[3][0] == listVehicles[2][3] == 1:
    flag = False

# check r
if listVehicles[0][2] == listVehicles[0][3] == 1:
    flag = False
if listVehicles[1][2] == listVehicles[1][3] == 1:
    flag = False
if listVehicles[2][2] == listVehicles[2][3] == 1:
    flag = False
if listVehicles[3][2] == listVehicles[3][3] == 1:
    flag = False

# check s
if listVehicles[0][1] == listVehicles[1][1] == 1 or listVehicles[0][1] == listVehicles[3][1] == 1:
    flag = False

if listVehicles[1][1] == listVehicles[2][1] == 1 or listVehicles[1][1] == listVehicles[0][1] == 1:
    flag = False

if listVehicles[2][1] == listVehicles[1][1] == 1 or listVehicles[2][1] == listVehicles[3][1] == 1:
    flag = False

if listVehicles[3][1] == listVehicles[0][1] == 1 or listVehicles[3][1] == listVehicles[2][1] == 1:
    flag = False

# check p
if listVehicles[0][3] == listVehicles[0][1] == 1:
    flag = False

if listVehicles[1][3] == listVehicles[1][1] == 1:
    flag = False

if listVehicles[2][3] == listVehicles[2][1] == 1:
    flag = False

if listVehicles[3][3] == listVehicles[3][1] == 1:
    flag = False

if flag == True:
    print("NO")
else:
    print("YES")