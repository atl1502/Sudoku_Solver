#Test boards
valid_sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
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
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
invalid_sudoku_board2 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5, 0, 0, 0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 9, 0, 6, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8, 0],
                        [0, 0, 0, 4, 1, 9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
#Checking that the board inputted is actually a valid board
def check_for_valid_board(board):
#The location of each number in tuples (column, row) sorted by number
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixes = []
    sevens = []
    eights = []
    nines = []
    all_numbers = [ones, twos, threes, fours, fives, sixes, sevens, eights, nines]
    return_value = True
#Sorting all the numbers into respective array
    for row, row_num in zip(board, range(1, 10)):
        for num, column_num in zip(row, range(1, 10)):
            if num == 1:
                ones.append((column_num, row_num))
            elif num == 2:
                twos.append((column_num, row_num))
            elif num == 3:
                threes.append((column_num, row_num))
            elif num == 4:
                fours.append((column_num, row_num))
            elif num == 5:
                fives.append((column_num, row_num))
            elif num == 6:
                sixes.append((column_num, row_num))
            elif num == 7:
                sevens.append((column_num, row_num))
            elif num == 8:
                eights.append((column_num, row_num))
            elif num == 9:
                nines.append((column_num, row_num))
    for number in all_numbers:
        return_value = do_rules_work(number)

#Checking no number is in the same row, column or box as any of the other numbers.
def do_rules_work(array_num):
    column = []
    row = []
    for column_locations, row_locations in array_num:
        column.append(column_locations)
        row.append(row_locations)
    column.sort()
    row.sort()

check_for_valid_board(valid_sudoku_board)
