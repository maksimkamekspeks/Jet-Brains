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
                if (point[0] == "start") and (point[1] == "easy" or point[1] == "user" or point[1] == "medium"
                                              or point[1] == "hard") \
                        and (point[2] == "easy" or point[2] == "user" or point[2] == "medium" or point[2] == "hard"):
                    if point[1] == "user" and point[2] == "user":
                        return "user", "user"
                    elif point[1] == "user" and point[2] == "easy":
                        return "user", "easy"
                    elif point[1] == "easy" and point[2] == "user":
                        return "easy", "user"
                    elif point[1] == "easy" and point[2] == "easy":
                        return "easy", "easy"
                    elif point[1] == "medium" and point[2] == "user":
                        return "medium", "user"
                    elif point[1] == "user" and point[2] == "medium":
                        return "user", "medium"
                    elif point[1] == "easy" and point[2] == "medium":
                        return "easy", "medium"
                    elif point[1] == "medium" and point[2] == "easy":
                        return "medium", "easy"
                    elif point[1] == "medium" and point[2] == "medium":
                        return "medium", "medium"
                    elif point[1] == "user" and point[2] == "hard":
                        return "user", "hard"
                    elif point[1] == "hard" and point[2] == "user":
                        return "hard", "user"
                    elif point[1] == "hard" and point[2] == "hard":
                        return "hard", "hard"
                else:
                    print("Bad parameters!")
            else:
                print("Bad parameters!")


def main_logic(first, second):
    # Creating list for table
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
        print(f"""---------
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
            for coordinate in coordinates:
                if coordinate == " " and len(coordinates) > 3:
                    coordinates.remove(coordinate)
            return coordinates
            # if len(coordinates) == 3:
            # if coordinates[0].isdigit() and coordinates[2].isdigit() and coordinates[1] == " ":
            # return coordinates
            # else:
            # print("Your answer should be like this: 'number space number'")
            # else:
            # print("Your answer should be like this: 'number space number'")

    # Take all possible moves for AI_easy
    def AI_easy_move():
        jey_1 = []
        for q in range(3):
            for w in range(3):
                if a_1[q][w] == " ":
                    jey_1.append(str(q + 1) + str(w + 1))
        print('Making move level "easy"')
        row = random.choice(jey_1)
        low = list(row)
        b[0] = low[0]
        b[2] = low[1]

    # Take all possible moves for AI_medium
    def AI_medium_move(first_1):
        # jey_4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        jey_1 = []
        jey_2 = []
        jey_3 = []
        for q in range(3):
            for w in range(3):
                if a_1[q][w] == " ":
                    jey_1.append(str(q + 1) + str(w + 1))
        if first_1 == "medium":
            fur = "X"
            qwe = "O"
        else:
            fur = "O"
            qwe = "X"
        while True:
            # Horizontal variants
            if a_1[0][0] == a_1[0][1] == fur:
                xyz = str(1) + str(3)
                jey_2.append(xyz)
            if a_1[0][1] == a_1[0][2] == fur:
                xyz = str(1) + str(1)
                jey_2.append(xyz)
            if a_1[1][0] == a_1[1][1] == fur:
                xyz = str(2) + str(3)
                jey_2.append(xyz)
            if a_1[1][1] == a_1[1][2] == fur:
                xyz = str(2) + str(1)
                jey_2.append(xyz)
            if a_1[2][0] == a_1[2][1] == fur:
                xyz = str(3) + str(3)
                jey_2.append(xyz)
            if a_1[2][1] == a_1[2][2] == fur:
                xyz = str(3) + str(1)
                jey_2.append(xyz)

            # Vertical variants
            if a_1[0][0] == a_1[1][0] == fur:
                xyz = str(3) + str(1)
                jey_2.append(xyz)
            if a_1[1][0] == a_1[2][0] == fur:
                xyz = str(1) + str(1)
                jey_2.append(xyz)
            if a_1[0][1] == a_1[1][1] == fur:
                xyz = str(3) + str(2)
                jey_2.append(xyz)
            if a_1[1][1] == a_1[2][1] == fur:
                xyz = str(1) + str(2)
                jey_2.append(xyz)
            if a_1[0][2] == a_1[1][2] == fur:
                xyz = str(3) + str(3)
                jey_2.append(xyz)
            if a_1[2][2] == a_1[1][2] == fur:
                xyz = str(1) + str(3)
                jey_2.append(xyz)

            # Diagonal variants
            if a_1[0][0] == a_1[1][1] == fur:
                xyz = str(3) + str(3)
                jey_2.append(xyz)
            if a_1[1][1] == a_1[2][2] == fur:
                xyz = str(1) + str(1)
                jey_2.append(xyz)
            if a_1[0][2] == a_1[1][1] == fur:
                xyz = str(3) + str(1)
                jey_2.append(xyz)
            if a_1[2][0] == a_1[1][1] == fur:
                xyz = str(1) + str(3)
                jey_2.append(xyz)

            # def table_1():
            #   print(f"""
            # ---------
            # | {a_1[0][0]} {a_1[0][1]} {a_1[0][2]} |
            # | {a_1[1][0]} {a_1[1][1]} {a_1[1][2]} |
            # | {a_1[2][0]} {a_1[2][1]} {a_1[2][2]} |
            # ---------""")

            for i in range(len(jey_1)):
                for n in range(len(jey_2)):
                    if jey_2[n] == jey_1[i]:
                        jey_3.append(jey_2[n])
            if len(jey_3) != 0:
                row = random.choice(jey_3)
                low = list(row)
                b[0] = low[0]
                b[2] = low[1]
                break
            if fur == qwe:
                break
            fur = qwe
        if len(jey_3) == 0:
            row = random.choice(jey_1)
            low = list(row)
            b[0] = low[0]
            b[2] = low[1]
        print('Making move level "medium"')
        # exit()

    # Take all possible moves for AI_hard if hard versus hard
    def AI_hard_move_2(inc_1):
        print('Making move level "hard"')
        if inc_1 == 1:
            ai = "X"
        else:
            ai = "O"
        bestScore = -10000
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                if a_1[i][j] == " ":
                    a_1[i][j] = ai
                    score = minimax_2(a_1, 0, False, inc_1)
                    a_1[i][j] = " "
                    if score > bestScore:
                        bestScore = score
                        move[0] = i
                        move[1] = j
        # a_1[move[0]][move[1]] = ai
        b[0] = str(move[0] + 1)
        b[2] = str(move[1] + 1)

    def minimax_2(a_1, depth, isMaximizing, inc_1):
        if inc == 1:
            ai = "X"
            human = "O"
            scores = {"X": 10, "O": -10, "Draw": 0, None: 1}
        else:
            ai = "O"
            human = "X"
            scores = {"O": 10, "X": -10, "Draw": 0, None: 1}
        result = checkWinner()
        if result is not None:
            return scores[result]
        if isMaximizing:
            bestScore = - 10000
            for i in range(3):
                for j in range(3):
                    if a_1[i][j] == " ":
                        a_1[i][j] = ai
                        score = minimax_2(a_1, depth + 1, False, inc_1)
                        a_1[i][j] = " "
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = 10000
            for i in range(3):
                for j in range(3):
                    if a_1[i][j] == " ":
                        a_1[i][j] = human
                        score = minimax_2(a_1, depth + 1, True, inc_1)
                        a_1[i][j] = " "
                        bestScore = min(score, bestScore)
            return bestScore

    # Take all possible moves for AI_hard
    def AI_hard_move(first_1):
        print('Making move level "hard"')
        if first_1 == "hard":
            ai = "X"
        else:
            ai = "O"
        bestScore = -10000
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                if a_1[i][j] == " ":
                    a_1[i][j] = ai
                    score = minimax(a_1, 0, False, first_1)
                    a_1[i][j] = " "
                    if score > bestScore:
                        bestScore = score
                        move[0] = i
                        move[1] = j
        # a_1[move[0]][move[1]] = ai
        b[0] = str(move[0] + 1)
        b[2] = str(move[1] + 1)

    def minimax(a_1, depth, isMaximizing, first_1):
        if first_1 == "hard":
            ai = "X"
            human = "O"
            scores = {"X": 10, "O": -10, "Draw": 0, None: 1}
        else:
            ai = "O"
            human = "X"
            scores = {"O": 10, "X": -10, "Draw": 0, None: 1}
        result = checkWinner()
        if result is not None:
            return scores[result]
        if isMaximizing:
            bestScore = - 10000
            for i in range(3):
                for j in range(3):
                    if a_1[i][j] == " ":
                        a_1[i][j] = ai
                        score = minimax(a_1, depth + 1, False, first_1)
                        a_1[i][j] = " "
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = 10000
            for i in range(3):
                for j in range(3):
                    if a_1[i][j] == " ":
                        a_1[i][j] = human
                        score = minimax(a_1, depth + 1, True, first_1)
                        a_1[i][j] = " "
                        bestScore = min(score, bestScore)
            return bestScore

    def checkWinner():
        winner = None
        # Checking horizontal and vertical variants
        for m in range(3):
            if a_1[m][0] == a_1[m][1] == a_1[m][2] == "X":
                winner = "X"
            if a_1[0][m] == a_1[1][m] == a_1[2][m] == "X":
                winner = "X"
        for m in range(3):
            if a_1[m][0] == a_1[m][1] == a_1[m][2] == "O":
                winner = "O"
            if a_1[0][m] == a_1[1][m] == a_1[2][m] == "O":
                winner = "O"
        # Checking diagonal variants (exit from "while" already in conditions)
        if a_1[0][0] == a_1[1][1] == a_1[2][2] == "X":
            winner = "X"
        if a_1[0][0] == a_1[1][1] == a_1[2][2] == "O":
            winner = "O"
        if a_1[2][0] == a_1[1][1] == a_1[0][2] == "X":
            winner = "X"
        if a_1[2][0] == a_1[1][1] == a_1[0][2] == "O":
            winner = "O"
        openSpots = 0
        for i in range(3):
            for n in range(3):
                if a_1[i][n] == " ":
                    openSpots += 1
        if winner is None and openSpots == 0:
            return "Draw"
        else:
            return winner

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
                AI_easy_move()
                pass
            else:
                b = input_coord()
        if first == "easy" and second == "user":
            if x > y:
                b = input_coord()
                pass
            else:
                AI_easy_move()
        if first == "easy" and second == "easy":
            if x > y:
                AI_easy_move()
            else:
                AI_easy_move()
        if first == "user" and second == "medium":
            if x > y:
                AI_medium_move(first)
                pass
            else:
                b = input_coord()
        if first == "medium" and second == "user":
            if x > y:
                b = input_coord()
                pass
            else:
                AI_medium_move(first)
        if first == "medium" and second == "medium":
            if x > y:
                AI_medium_move(first)
            else:
                AI_medium_move(first)
        if first == "easy" and second == "medium":
            if x > y:
                AI_medium_move(first)
                pass
            else:
                AI_easy_move()
        if first == "medium" and second == "easy":
            if x > y:
                AI_easy_move()
                pass
            else:
                AI_medium_move(first)
        if first == "user" and second == "hard":
            if x > y:
                AI_hard_move(first)
                pass
            else:
                b = input_coord()
        if first == "hard" and second == "user":
            if x > y:
                b = input_coord()
                pass
            else:
                AI_hard_move(first)
        if first == "hard" and second == "hard":
            if x > y:
                inc = 0
                AI_hard_move_2(inc)
                pass
            else:
                inc = 1
                AI_hard_move_2(inc)

        # Judge!
        if b[0].isdigit() and b[2].isdigit() and b[1] == " ":
            if (4 > int(b[0]) > 0) and (4 > int(b[2]) > 0):
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


sys.setrecursionlimit(1000)
main()
