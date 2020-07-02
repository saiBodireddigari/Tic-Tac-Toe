game_input = input("Enter cells: ")
game_list = list(game_input)
matrix = []


def matrix_init(x_or_o):
    for row in range(3):
        row_list = [x_or_o[3 * row + column] for column in range(3)
                    if "X" in x_or_o or "O" in x_or_o or "-" in x_or_o]
        matrix.append(row_list)


def matrix_printing(x_o_matrix):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(x_o_matrix[i][j], end=" ")
        print("|")
    print("---------")


matrix_init(game_list)
matrix_printing(matrix)


def matrix_check(x_o_matrix, position_list):
    row_matrix = []
    for position in position_list:
        x = position[0]
        y = position[1]
        row_matrix.append(x_o_matrix[x][y])
    return row_matrix


def game():
    count_x = 0
    count_o = 0

    win_series_x = ["X", "X", "X"]
    win_series_0 = ["O", "O", "O"]

    col_0 = matrix_check(matrix, [[0, 0], [0, 1], [0, 2]])
    col_1 = matrix_check(matrix, [[1, 0], [1, 1], [1, 2]])
    col_2 = matrix_check(matrix, [[2, 0], [2, 1], [2, 2]])
    cross_1 = matrix_check(matrix, [[0, 0], [1, 1], [2, 2]])
    cross_2 = matrix_check(matrix, [[0, 2], [1, 1], [2, 0]])
    row_0 = matrix_check(matrix, [[0, 0], [1, 0], [2, 0]])
    row_1 = matrix_check(matrix, [[0, 1], [1, 1], [2, 1]])
    row_2 = matrix_check(matrix, [[0, 2], [1, 2], [2, 2]])

    winner_is_x = (col_0 == win_series_x) or (col_1 == win_series_x) or \
                  (col_2 == win_series_x) or (cross_1 == win_series_x) or \
                  (cross_2 == win_series_x) or (row_0 == win_series_x) or \
                  (row_1 == win_series_x) or (row_2 == win_series_x)
    winner_is_o = (col_0 == win_series_0) or (col_1 == win_series_0) or \
                  (col_2 == win_series_0) or (cross_1 == win_series_0) or \
                  (cross_2 == win_series_0) or (row_0 == win_series_0) or \
                  (row_1 == win_series_0) or (row_2 == win_series_0)

    for X_O in game_list:
        if X_O == "X":
            count_x += 1
        elif X_O == "O":
            count_o += 1

    while winner_is_x:
        if not winner_is_o:
            print("X wins")
            break
        elif winner_is_o:
            print("Impossible")
            break
    else:
        if winner_is_o:
            print("O wins")
        elif ("_" not in game_list) and not winner_is_o and not winner_is_x:
            print("Draw")
        elif abs(count_x - count_o) >= 2:
            print("Impossible")
        else:
            print("Game not finished")


game()
