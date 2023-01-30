from clart import *

user_board = []

def print_board(board):

    print("\n- - - - - - - - - - - - -")

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")

            print(f"{board[i][j]} ", end="")

        print("|")

    print("- - - - - - - - - - - - -")



def find_empty_space(board):

    for i in range(9):

        for j in range(9):

            if board[i][j] == 0:
                return (i, j)
    return None



def validate_guess(board, guess, position):

    # Check the current row
    for i in range(9):
        if board[position[0]][i] == guess and position[1] != i:
            return False


    # Check the current column
    for i in range(9):
        if board[i][position[1]] == guess and position[0] != i:
            return False



    # Check the current 3x3 box
    box_coordinate = (position[0] // 3, position[1] // 3)

    for i in range(box_coordinate[0] * 3, box_coordinate[0] * 3 + 3):

        for j in range(box_coordinate[1] * 3, box_coordinate[1] * 3 + 3):

            if board[i][j] == guess and (i, j) != position:
                return False


    # Passed all checks
    return True



def solve_board(board):
    found = find_empty_space(board)

    if not found:
        return True
    else:
        row, column = found

    for i in range(1, 10):
        if validate_guess(board, i, (row, column)):
            board[row][column] = i

            if solve_board(board):
                return True

            board[row][column] = 0

    return False



def build_board():
    """
    Takes user input line-by-line until all numbers received.
    Builds 2-D Array formatted for use with the print_board() function
    """

    for i in range(1, 10):
        line_numbers = []
        num_input = input(f"\nPlease enter the numbers in line #{i}\nUse 0 for all empty spaces\nType all 9 numbers together and press [enter] when done:  ")
        for num in num_input:
            try:
                line_numbers.append(int(num))
            except ValueError:
                break
                reset_board()
        user_board.append(line_numbers)


def is_valid_sudoku(board):
    for i in range(9):
        if len(board[i]) != 9:
            return False

        for entry in board[i]:
            if not isinstance(entry, int):
                return False

        row_set = set()

        for j in range(9):

            current_value = board[i][j]

            # Ignore blank spaces
            if current_value == 0:
                continue
            if current_value in row_set:
                return False
            row_set.add(current_value)

            # Check the full column
            for row_num in range(9):
                if board[row_num][j] == current_value and row_num != i:
                    return False


            # Check the box current value is in
            # Will give box coordinate (0-2, 0-2)
            x_box = j // 3   #x-axis (column)
            y_box = i // 3   #y-axis (row)

            for y_num in range(y_box * 3, y_box * 3 + 3):
                for x_num in range(x_box * 3, x_box * 3 + 3):

                    if board[y_num][x_num] == current_value and (y_num, x_num) != (i, j):
                        return False

    return True


def reset_board():
    global user_board
    print(error_text)
    print("It seems there was an error.")
    print("To be valid, your board must contain 9 rows of boxes with 9 numbers in each.")
    print("Every entry must be a whole number.")
    print("There can be no repeat numbers in rows, columns, or boxes.")
    print("Please try again.\n\n")
    user_board = []
    build_board()


def start_app():

    print(welcome_text)
    build_board()

    while not is_valid_sudoku(user_board):
        reset_board()

    print(input_board_text)
    print_board(user_board)
    print(solved_board_text)
    solve_board(user_board)
    print_board(user_board)
    print("\n\n\n")