rows = ["#        |     |   ","#        |     |   ", "#   _____|_____|_____", "#        |     |   ", "#        |     |   ", "#   _____|_____|_____", "#        |     |   ", "#        |     |   ", "#        |     |   " ]
circle = True
PlaceIndex = 0
coords=""
index=0
thisdict = {
    "1/1": [1, 6],
    "1/2": [1, 12],
    "1/3": [1, 18],
    "2/1": [4, 6],
    "2/2": [4, 12],
    "2/3": [4, 18],
    "3/1": [7, 6],
    "3/2": [7, 12],
    "3/3": [7, 18]
}
possibleLocations = ["1/1", "1/2", "1/3", "2/1", "2/2", "2/3", "3/1", "3/2", "3/3"]

WINNING_COMBINATIONS = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]
for j in range(9):
    index = index + 1
    if j != 0:
        print("Enter two numbers between 1 and 3 to choose first the row, then the column in the format [ROW/COLUMN]")
        coords = input()
        circle = not circle
    def create_grid():
        if circle:
            toPlace="O"
        if not circle:
            toPlace = "X"
        for key in thisdict:
                if key == coords:
                    if key in possibleLocations:
                        arr = list(rows[thisdict[key][0]])
                        arr[thisdict[key][1]] = toPlace
                        rows[thisdict[key][0]] = "".join(arr)
                        possibleLocations[possibleLocations.index(key)] = toPlace
                        #global circle 
                        #does not work????
                        #circle = not circle
                    else:
                        print("This position is not possible to place something")
                        #do not change circle boolean
        for x in rows:
            print(x)
    def check_win():
        for combination in WINNING_COMBINATIONS:
            if possibleLocations[combination[0]] == "X" and possibleLocations[combination[1]] == "X" and possibleLocations[combination[2]] == "X":
                print("X has won !")
            if possibleLocations[combination[0]] == "O" and possibleLocations[combination[1]] == "O" and possibleLocations[combination[2]] == "O":
                print("O has won !")
            elif index == 9:
                print("It's a draw")
    create_grid()
    check_win()
        #check for draw
