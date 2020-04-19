# Location-Game
Location Game 

This Location Game is used to eleborate the uses of List and Dict :

locations = {
    0: "You are sitting in the front of a computer learning Python ",
    1: "You are standing end of a road before a small bricks building",
    2: "You are at the top of the Hill",
    3: "You are inside the building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest"
}

Here 0,1,2,3,4,5 are representing Dict keys and Dict values represents different directions.


exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S":4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

Here Q - Exits 
     W - West
     N - North 
     S - South
     E - East
 
Here loc = 1 represent initial location which is road in our code

Here we have used join, upper and Break function.

join :-  join() function to join a list of strings

upper :- The upper() methods returns the uppercased string from the given string. It converts all lowercase characters to uppercase. If no lowercase characters exist, it returns the original string.

break :- The break is a keyword in python which is used to bring the program control out of the loop.
