# write your code here

# things = input()
# thingsList = list(things)
# a = [i.replace("_", " ") for i in thingsList]


import random

# Creating lists for table
empty = " "


def create_a_1():
    e_1 = [[], [], []]
    for h in range(3):
        for j in range(3):
            e_1[h].append(empty)
    return e_1


a_1 = create_a_1()


def create_a():
    e = []
    for h in range(9):
        e.append(empty)
    return e


a = create_a()

# Maybe we need another type of list for purposes


def table():
    print(f"""---------
| {a[0]} {a[1]} {a[2]} |
| {a[3]} {a[4]} {a[5]} |
| {a[6]} {a[7]} {a[8]} |
---------""")


# Printing current situation

def table_1():
    print(f"""
---------
| {a_1[0][0]} {a_1[0][1]} {a_1[0][2]} |
| {a_1[1][0]} {a_1[1][1]} {a_1[1][2]} |
| {a_1[2][0]} {a_1[2][1]} {a_1[2][2]} |
---------""")

# input from person


def input_coord():
    current_coord = input('Enter the coordinates: ')
    current_coord_list = list(current_coord)
    coordinates = current_coord_list
    return coordinates


jey = []
b = []
f = True
f_1 = True
x = 0
y = 0
table_1()

# Main cycle of analyzing moves

while f:
    # Calculating X and O
    for r in range(3):
        for s in range(3):
            if a_1[r][s] == "X":
                x += 1
            elif a_1[r][s] == "O":
                y += 1

    # Take all possible moves for AI
    if x > y:
        for s in range(3):
            for z in range(3):
                if a_1[s][z] == " ":
                    jey.append(str(s + 1) + str(z + 1))
        print('Making move level "easy"')
        row = random.choice(jey)
        low = list(row)
        b[0] = low[0]
        b[2] = low[1]
        jey = []
        pass
    else:
        b = input_coord()

    # Judge!

    if b[0].isdigit() and b[2].isdigit() and b[1] == " ":
        if (4 > int(b[0]) > 0) and (4 > int(b[2]) > 0):

            # If occupied?
            b_1 = int(b[0])
            b_2 = int(b[2])
            b_11 = b_1 - 1
            b_22 = b_2 - 1

            if a_1[b_11][b_22] == "X" or a_1[b_11][b_22] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            elif x > y:
                a_1[b_11][b_22] = "O"
                table_1()
            elif y == x:
                a_1[b_11][b_22] = "X"
                table_1()

            # Checking horizontal and vertical variants
            for s in range(3):
                if a_1[s][0] == a_1[s][1] == a_1[s][2] == "X":
                    print("X wins")
                    f = False
                    break
                if a_1[0][s] == a_1[1][s] == a_1[2][s] == "X":
                    print("X wins")
                    f = False
                    break
            for s in range(3):
                if a_1[s][0] == a_1[s][1] == a_1[s][2] == "O":
                    print("O wins")
                    f = False
                    break
                if a_1[0][s] == a_1[1][s] == a_1[2][s] == "O":
                    print("O wins")
                    f = False
                    break

            # If horizontal or vertical variant is winner, we finish
            if f:
                pass
            else:
                break

            # Checking diagonal variants (exit from "while" already in conditions)
            if a_1[0][0] == a_1[1][1] == a_1[2][2] == "X":
                print("X wins")
                break
            if a_1[0][0] == a_1[1][1] == a_1[2][2] == "O":
                print("O wins")
                break
            if a_1[2][0] == a_1[1][1] == a_1[0][2] == "X":
                print("X wins")
                break
            if a_1[2][0] == a_1[1][1] == a_1[0][2] == "O":
                print("O wins")
                break

            # Does on board exist places to move?
            for s in range(3):
                if not f_1:
                    break
                for z in range(3):
                    if a_1[s][z] == " ":
                        f_1 = False
                        break

            # Next calculating of move for AI might start from begin (X = 0, O = 0)
            x = 0
            y = 0

            # Draw if board is full
            if f_1:
                print("Draw")
                break
            else:
                continue
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
