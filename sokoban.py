
world_shape = (5,6)

EMPTY = 0
WALL = 1
PLAYER = 2
BOX = 3
MARKER = 4
PLAYER_MARKER = 5
BOX_MARKER = 6
PLAYER_MOVING = 7
PUSH = 8

tiles = " NS#!$%Rp"
world = [1,2,0,0,0,0,1]
while input() != "e":
    print("_")
    for k in range(len(world)):
        current_cell = world[k]
        if current_cell == PLAYER:
            current_cell = PLAYER_MOVING
        elif current_cell == EMPTY:
            if world[k-1] == PLAYER_MOVING:
                current_cell = PLAYER
        elif current_cell == PLAYER_MOVING:
            current_cell = EMPTY
        elif current_cell == BOX:
            if world[k-1] == PLAYER_MOVING:
                current_cell = PUSH
            
        world[k] = current_cell
        print(tiles[world[k]], end="")
    print()

