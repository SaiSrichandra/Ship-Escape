import game
from game import *
overall_path = []
import_ship("ship_layout.txt") 
place_pieces(Bot, Alien, Crew, 10)
fno = input("Enter File number : ")
fname = r"test_files\bot2\run{}.txt".format(fno)
f = open(fname,"w")

while True:
    
    # global ship
    # back_track = game.ship.shape[0] + 1
    # print("\033[A" * back_track)
    print("----------------------------------------------------------------------------------------------------------------", file = f)
    print_ship(f = f)
    
    cur_path = A_star_algo()
    # If current path is 
    if not cur_path:
        move_aliens()
        continue
    overall_path.append(cur_path[0])
    if cur_path[1] in [game.crew_pos]:
        overall_path.append(cur_path[1])
        break
    game.ship[cur_path[0][0],cur_path[0][1]] = 1
    game.ship[cur_path[1][0],cur_path[1][1]] = game.Bot
    game.bot_pos = (cur_path[1][0],cur_path[1][1])
    
    
    
    # print("\033[A" * back_track)
    
    # time.sleep(3)
    move_aliens()
    print(cur_path, file = f)
    print("------------------------------------------------------------------", file = f)
    


print(overall_path, file = f)







