import numpy as np
d = int(input('enter dimensions of ship'))
# A ship is created with all blocked cells represented by 0s
ship = np.zeros([d,d,2], dtype=int)

# Opening a random cell, open state is 1
posX,posY = np.random.randint(d,size = 2)
print(posX)
print(posY)
ship[posX,posY,0] = 1

# Updating the neughbours
for i in [[0,1],[0,-1],[1,0],[-1,0]]:
    if posX+i[0] >=0 and posY+i[1]>=0 and posX+i[0] < d and posY+i[1] < d:
        ship[posX+i[0],posY+i[1],1] += 1

for i in range(0,d):
    for j in range(0,d):
        print(str(ship[i,j,0]), end=" ")
    print("\n")

print("\n")
print("\n")

for i in range(0,d):
    for j in range(0,d):
        print(str(ship[i,j,1]), end=" ")
    print("\n")

print("\n")

while True:

    one_adj_list = np.where(ship[:,:,1] == 1)
    
    if len(one_adj_list) == 0:
        break
    next_pos = np.random.randint(len(one_adj_list[0]),size=1)
    posX = one_adj_list[0][next_pos]
    posY = one_adj_list[1][next_pos]
    if ship[posX,posY,0] == 1:
        continue
    ship[posX,posY,0] = 1
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        if posX+i[0] >=0 and posY+i[1]>=0 and posX+i[0] < d and posY+i[1] < d:
            ship[posX+i[0],posY+i[1],1] += 1


    for i in range(0,d):
        for j in range(0,d):
            print(str(ship[i,j,0]), end=" ")
        print("\n")

    print("\n")

    for i in range(0,d):
        for j in range(0,d):
            print(str(ship[i,j,1]), end=" ")
        print("\n")

    print("-------------------------------------------------------------")


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

for i in range(0,d):
    for j in range(0,d):
        print(str(ship[i,j,0]), end=" ")
    print("\n")

print("\n")

for i in range(0,d):
    for j in range(0,d):
        print(str(ship[i,j,1]), end=" ")
    print("\n")

