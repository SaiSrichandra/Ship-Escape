import numpy as np
import random
d = int(input('enter dimensions of ship'))
# A ship is created with all blocked cells represented by 0s
ship = np.zeros([d,d,2], dtype=int)

# Opening a random cell, open state is 1
posX,posY = np.random.randint(d,size = 2)
# print(posX)
# print(posY)
ship[posX,posY,0] = 1

# Updating the neughbours
for i in [[0,1],[0,-1],[1,0],[-1,0]]:
    if posX+i[0] >=0 and posY+i[1]>=0 and posX+i[0] < d and posY+i[1] < d:
        ship[posX+i[0],posY+i[1],1] += 1

# for i in range(0,d):
#     for j in range(0,d):
#         print(str(ship[i,j,0]), end=" ")
#     print("\n")

# print("\n")
# print("\n")

# for i in range(0,d):
#     for j in range(0,d):
#         print(str(ship[i,j,1]), end=" ")
#     print("\n")

# print("\n")

while True:

    one_adj_list = np.where(ship[:,:,1] == 1)
    one_adj_list_temp = [np.array([], dtype=int), np.array([], dtype=int)]
    for i in range(len(one_adj_list[0])):
        if ship[one_adj_list[0][i],one_adj_list[1][i],0] == 0:
            one_adj_list_temp[0] = np.append(one_adj_list_temp[0], one_adj_list[0][i])
            one_adj_list_temp[1]= np.append(one_adj_list_temp[1], one_adj_list[1][i])
    one_adj_list = tuple(one_adj_list_temp)
    one_adj_list_temp = None
    if len(one_adj_list[0]) == 0:
        break
    next_pos = np.random.randint(len(one_adj_list[0]),size=1)
    # print(next_pos)
    posX = one_adj_list[0][next_pos]
    posY = one_adj_list[1][next_pos]
    # print(posX)
    # print(posY)
    if ship[posX,posY,0] == 1:
        continue
    ship[posX,posY,0] = 1
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        if posX+i[0] >=0 and posY+i[1]>=0 and posX+i[0] < d and posY+i[1] < d:
            ship[posX+i[0],posY+i[1],1] += 1


#     for i in range(0,d):
#         for j in range(0,d):
#             print(str(ship[i,j,0]), end=" ")
#         print("\n")

#     print("\n")

#     for i in range(0,d):
#         for j in range(0,d):
#             print(str(ship[i,j,1]), end=" ")
#         print("\n")

#     print("-------------------------------------------------------------")


# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# for i in range(0,d):
#     for j in range(0,d):
#         print(str(ship[i,j,0]), end=" ")
#     print("\n")

# print("\n")


# Choosing half of the dead ends at random


dead_list = np.where(ship[:,:,1] == 1)
# print(dead_list)
random_dead = random.sample([i for i in range(len(dead_list[0]))], len(dead_list[0])//2)
# print(random_dead)
half_dead = list(map(lambda x : (dead_list[0][x], dead_list[1][x]), random_dead))
# print(half_dead)
# print(len(half_dead))
try:
    for i in range(len(half_dead)):
        posX,posY = half_dead[i]
        adj_coord = [[posX+1,posY],[posX-1,posY],[posX,posY+1],[posX,posY-1]]
        adj_coord_temp = []
        for k in adj_coord:
            if k[0] < 0 or k[1]<0 or k[0]>=d or k[1]>=d or ship[k[0],k[1],0] == 1:
                continue
            else:   
                adj_coord_temp.append(k)
        opX,opY = random.choice(adj_coord_temp)
        ship[opX,opY,0] = 1

except:
    print(ship[half_dead[i][0],half_dead[i][1],0])
    print(ship[half_dead[i][0],half_dead[i][1],1])
    print(adj_coord)
    print(adj_coord_temp)
    print(k)
    print(opX)
    print(opY)
    print()
    np.savetxt("ship.txt", X=ship[:,:,0],fmt="%d",delimiter="")
    np.savetxt("neigh.txt", X=ship[:,:,1],fmt="%d",delimiter="")
    exit(0)

# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Final ship layout is :\n\n")
for i in range(0,d):
    for j in range(0,d):
        print(str(ship[i,j,0]), end=" ")
    print("\n")

print("\n")
