game_input = list("         ")


def matrix_init(x_o_list_input):
    matrix = []
    for row in range(3):
        row_list = [x_o_list_input[3 * row + column] for column in range(3)]
        matrix.append(row_list)
    return matrix


def matrix_printing(game_list_matrix):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(game_list_matrix[i][j], end=" ")
        print("|")
    print("---------")


def winner_check(current_state_list, count):
    col1 = current_state_list[0:3]
    col2 = current_state_list[3:6]
    col3 = current_state_list[6:9]
    row1 = current_state_list[0:7:3]
    row2 = current_state_list[1:8:3]
    row3 = current_state_list[2:9:3]
    cross1 = current_state_list[0:9:4]
    cross2 = current_state_list[2:7:2]

    result_matrix = [col1, col2, col3, row1, row2, row3, cross1, cross2]

    if ["X", "X", "X"] in result_matrix:
        print("X wins")
        determine_result = True
    elif ["O", "O", "O"] in result_matrix:
        print("O wins")
        determine_result = True
    elif len(current_state_list) == 9 and not (["X", "X", "X"] in result_matrix) \
            and not (["O", "O", "O"] in result_matrix) and count > 9:
        print("Draw")
        determine_result = True
    else:
        determine_result = False

    return determine_result


def play_the_game():
    counter = 1
    while True:
        coordinates = list(input("Enter the coordinates: "))
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[len(coordinates) - 1]
        if str.isnumeric(x_coordinate) and str.isnumeric(y_coordinate):
            if int(x_coordinate) in [1, 2, 3] and int(y_coordinate) in [1, 2, 3]:
                cells = [13, 23, 33, 12, 22, 32, 11, 21, 31]
                join_coordinates = int(x_coordinate + y_coordinate)
                if game_input[cells.index(join_coordinates)] not in ["X", "O"]:
                    if counter % 2 == 0:
                        game_input[cells.index(join_coordinates)] = "O"
                    else:
                        game_input[cells.index(join_coordinates)] = "X"
                    counter += 1
                    matrix_printing(matrix_init(game_input))

                    win = winner_check(game_input, counter)
                    if win:
                        break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


matrix_printing(matrix_init(game_input))
play_the_game()
