# write your code here

import random
import sys


def main():
    while True:
        p_1, p_2 = menu()
        main_logic(p_1, p_2)


def menu():
    while True:
        menu_stat = input()
        menu_stat_list = menu_stat.split(" ")
        point = menu_stat_list
        if menu_stat == "exit":
            sys.exit()
        if len(point) != 3:
            print("Bad parameters!")
        else:
            if isinstance(point[0], str) and isinstance(point[1], str) and isinstance(point[2], str):
                if (point[0] == "start") and (point[1] == "easy" or point[1] == "user") \
                        and (point[2] == "easy" or point[2] == "user"):
                    if point[1] == "user" and point[2] == "user":
                        return "user", "user"
                    elif point[1] == "user" and point[2] == "easy":
                        return "user", "easy"
                    elif point[1] == "easy" and point[2] == "user":
                        return "easy", "user"
                    elif point[1] == "easy" and point[2] == "easy":
                        return "easy", "easy"
                else:
                    print("Bad parameters!")
            else:
                print("Bad parameters!")


def main_logic(first, second):
    # Creating lists for table
    empty = " "

    def create_a_1():
        e_1 = [[], [], []]
        for h in range(3):
            for j in range(3):
                e_1[h].append(empty)
        return e_1

    a_1 = create_a_1()

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
        while True:
            current_coord = input('Enter the coordinates: ')
            if current_coord == "exit":
                sys.exit()
            current_coord_list = list(current_coord)
            coordinates = current_coord_list
            if len(coordinates) == 3:
                if coordinates[0].isdigit() and coordinates[2].isdigit() and coordinates[1] == " ":
                    return coordinates
                else:
                    print("Your answer should be like this: 'number space number'")
            else:
                print("Your answer should be like this: 'number space number'")

    # Take all possible moves for AI
    def AI_easy_move(jey_1):
        for q in range(3):
            for w in range(3):
                if a_1[q][w] == " ":
                    jey_1.append(str(q + 1) + str(w + 1))
        print('Making move level "easy"')
        row = random.choice(jey_1)
        low = list(row)
        b[0] = low[0]
        b[2] = low[1]

    jey = []
    b = [0, " ", 0]
    f = True
    x = 0
    y = 0
    table_1()

    # Main cycle of analyzing moves

    while f:
        f_1 = True
        # Calculating X and O
        for r in range(3):
            for s in range(3):
                if a_1[r][s] == "X":
                    x += 1
                elif a_1[r][s] == "O":
                    y += 1

        # Checking who is who
        if first == "user" and second == "user":
            b = input_coord()
        if first == "user" and second == "easy":
            if x > y:
                AI_easy_move(jey)
                jey = []
                pass
            else:
                b = input_coord()
        if first == "easy" and second == "user":
            if x > y:
                b = input_coord()
                pass
            else:
                AI_easy_move(jey)
                jey = []
        if first == "easy" and second == "easy":
            if x > y:
                AI_easy_move(jey)
                jey = []
            else:
                AI_easy_move(jey)
                jey = []

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

                # Next calculating of move for AI might start from begin (X = 0, O = 0)
                x = 0
                y = 0

                # Does on board exist places to move?
                for s in range(3):
                    if not f_1:
                        break
                    for z in range(3):
                        if a_1[s][z] == " ":
                            f_1 = False
                            break

                if not f_1:
                    continue

                # Draw if board is full
                if f_1:
                    print("Draw")
                    break
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


main()
