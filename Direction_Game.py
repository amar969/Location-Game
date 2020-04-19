# Direction Games

locations = {
    0: "You are sitting in the front of a computer learning Python ",
    1: "You are standing end of a road before a small bricks building",
    2: "You are at the top of the Hill",
    3: "You are inside the building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest"
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S":4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
