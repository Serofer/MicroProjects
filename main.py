rows = ["#        |     |   ","#        |     |   ", "#   _____|_____|_____", "#        |     |   ", "#        |     |   ", "#   _____|_____|_____", "#        |     |   ", "#        |     |   ", "#        |     |   " ]
circle = True
PlaceIndex = 0
coords=""
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
for j in range(9):
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
                   arr = list(rows[thisdict[key][0]])
                   arr[thisdict[key][1]] = toPlace
                   rows[thisdict[key][0]] = "".join(arr)
        for x in rows:
            print(x)
    create_grid()
        #check for win, then continue
        #check for draw
