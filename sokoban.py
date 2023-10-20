
world_shape = (5,6)

SPACE = 0
WALL = 1
PLAYER = 2
BOX = 3
MARKER = 4
PLAYER_MARKER = 5
BOX_MARKER = 6
PLAYER_MOVING = 7
PUSH = 8
SPACE_ASK = 9
PLAYER_READY = 10
BOX_FIXED = 11


# The core functions WRITE_VALUE and READ_FROM are to be replaced by something more mathematically concise. 
#   Still to be implimented is the handling of the goal zones, or as I refer to here as MARKER. I imagine this can be handled externally with a modulus 2 or like.
def read_from(cellValue):
    left = 1
    right = -1
    centre = 0
    if cellValue == WALL: return centre
    if cellValue == PLAYER: return right
    if cellValue == PLAYER_MOVING: return right
    if cellValue == PLAYER_READY: return centre
    if cellValue == SPACE: return left
    if cellValue == SPACE_ASK: return left
    if cellValue == BOX: return left
    if cellValue == BOX_FIXED: return left
    if cellValue == PUSH: return right
    return centre

# The core functions WRITE_VALUE and READ_FROM are to be replaced by something more mathematically concise. 
#   Still to be implimented is the handling of the goal zones, or as I refer to here as MARKER. I imagine this can be handled externally with a modulus 2 or like.
def write_value(cellValue, readValue):
    # ideally, this project is only a success if the reasoning behind why this function works is non-obvious.
    if cellValue == WALL: 
        return WALL
    if cellValue == PLAYER:
        if readValue == PLAYER_READY: return PLAYER_MOVING
        if readValue == PUSH: return PLAYER_MOVING
        return PLAYER
    if cellValue == PLAYER_MOVING:
        if readValue == PLAYER: return SPACE
        return PLAYER
    if cellValue == PLAYER_READY: 
        return PLAYER
    if cellValue == SPACE:
        if readValue == PLAYER: return PLAYER_READY
        if readValue == BOX: return SPACE_ASK
    if cellValue == SPACE_ASK:
        if readValue == PUSH: return BOX
        if readValue == BOX: return SPACE
    if cellValue == BOX:
        if readValue == PLAYER: return PUSH
        if readValue == BOX: return BOX_FIXED
        return BOX
    if cellValue == BOX_FIXED:
        if readValue == PLAYER: return PUSH
        if readValue == BOX: return BOX_FIXED
        return BOX_FIXED
    if cellValue == PUSH:
        if readValue == BOX: return PLAYER
        return BOX
    return SPACE
    

#       "01234567890123456789"
tiles = " |@X!$%MP?R%QQQQQQQ"

# this string tests the core functiuonality of sokoban, namely
#       moving but being stopped by a wall
#       pushing a box but being stopped by a wall
#       pushing a box but being stopped by another box
world = [1,0,0,2,1,0,0,3,0,2,1,0,0,3,0,3,0,2,1,0,3,0,2,1]

print("input ready, input e to exit")

while input() != "e":
    print("_")
    # Each user input will be realised by running this internal for loop twice.
    for k in range(len(world)):
        print(tiles[world[k]], end="")

        # This is the core that operates the game rule. Currently user direction is not implemented, but this will be realised by changing the direction the list is read through in the for loop, using linear indexing to handle the vertical vs horizontal cases.
        # The world operates as a psuedo cellular automata, with each cell being updated in-place based on its value and the value of a neighbour of its choice. Since this is in place, it is critical that the cells of the world be updated in the correct order
        currentCell = world[k]
        readPos = read_from(currentCell)
        readCell = world[k + readPos]

        world[k] = write_value(currentCell, readCell)
    
    print()

print("goodbye")
