#Test boards
import copy
valid_sudoku_board1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]]
invalid_sudoku_board1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                         [6, 0, 0, 1, 9, 5, 0, 0, 0],
                         [0, 9, 8, 0, 0, 0, 0, 6, 0],
                         [8, 0, 0, 0, 6, 0, 0, 0, 3],
                         [4, 0, 0, 8, 0, 3, 0, 0, 1],
                         [7, 0, 0, 0, 2, 0, 0, 0, 6],
                         [0, 6, 0, 0, 0, 0, 2, 8, 0],
                         [0, 1, 0, 4, 1, 9, 0, 0, 5],
                         [0, 0, 0, 0, 8, 0, 0, 7, 9]] #row 8 the ones don't work
invalid_sudoku_board2 = [[5, 3, 9, 0, 7, 0, 0, 0, 0],
                         [6, 0, 0, 1, 9, 5, 0, 0, 0],
                         [0, 9, 8, 0, 0, 0, 0, 6, 0],
                         [8, 0, 0, 0, 6, 0, 0, 0, 3],
                         [4, 0, 0, 8, 0, 3, 0, 0, 1],
                         [7, 0, 0, 0, 2, 0, 0, 0, 6],
                         [0, 6, 0, 0, 0, 0, 2, 8, 0],
                         [0, 0, 0, 4, 1, 9, 0, 0, 5],
                         [0, 0, 0, 0, 8, 0, 0, 7, 9]] #box 1 the nines don't work

def check_rules_at_point(x, y, test_number, updated_board):
#Checks rows and columns for numbers that might not work
    for column_or_row in range(9):
        if updated_board[column_or_row][x] == test_number:
            return False
        elif updated_board[y][column_or_row] == test_number:
            return False
#Checks to make sure number isn't inside the box
    box_starting_x_value = (x//3) * 3
    box_starting_y_value = (y//3) * 3
    for added_y_value in range(3):
        for added_x_value in range(3):
            if updated_board[box_starting_y_value + added_y_value][box_starting_x_value + added_x_value] == test_number:
                return False
    return True

"""Checking that the board inputted is actually a valid board"""
def check_for_valid_board(board):
#The location of each number in tuples (column, row) sorted by number in an array
    numbers = [[], [], [], [], [], [], [], [], []]
#Sorting all the numbers into respective array
    for row, row_num in zip(board, range(1, 10)):
        for num, column_num in zip(row, range(1, 10)):
            for number in range(9):
                if num == number + 1:
                    numbers[number].append((column_num, row_num))
#Checks each number follows sudoku rules
    for number in numbers:
        if not do_rules_work(number):
            return False
    return True
#Checking no number is in the same row, column or box as any of the other numbers.
def do_rules_work(array_num):
    return_value = False
#Information about each number sorted
    boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    column_location_list = []
    row_location_list = []
#Splits the locations of rows, columns and boxes into separate lists
    for column_location, row_location in array_num:
        column_location_list.append(column_location)
        row_location_list.append(row_location)
        i = -1
        for box_y_value in range(3):
            for box_x_value in range(3):
                if ((column_location > box_y_value * 3) and (column_location <=  (box_y_value * 3) + 3)) and ((row_location > box_x_value * 3) and (row_location <= (box_x_value * 3) + 3)):
                    boxes[i] += 1
                i += 1
#Checking the number follows the rules in terms of boxes
    for box in boxes:
        if box > 1:
            return False
#Checking the number follows the rules in terms of row/column.
    column_location_list.sort()
    row_location_list.sort()
    if check_for_line_issues(column_location_list) and check_for_line_issues(row_location_list):
        return_value = True
    return return_value
#Looks for issues with lines collisions
def check_for_line_issues(orientation):
    for i in range(len(orientation)):
        if orientation[i] == orientation [i-1]:
            return False
    return True

"""Actually solving the sudoku board"""
#This will be done via backtracking
returned_information = []
def return_solved_board(board):
#Backtracking recursion loop starts
    def solve(board):
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for number in range(1,10):
                        if check_rules_at_point(x, y, number, board):
                            board[y][x] = number
                            solve(board)
        #Where backtracking comes into play, if the solve method fails on the next cell than it resets current one.
                            board[y][x] = 0
        #Breaks out of recursion to try a differant number in cell prior
                    return
        #Stores a solved copy of a solution into global variable
        global returned_information
        returned_information.append(copy.deepcopy(board))
#Checks if the board can be solved or not
    if not check_for_valid_board(board):
        return "This board is not possible to solve."
    else:
        solve(board)
    return returned_information

print(return_solved_board(invalid_sudoku_board2))
