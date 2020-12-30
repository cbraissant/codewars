'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
'''


'''
My solution
Might need to be refactored to be more comprehensible
'''
def check_valid_numbers(numbers):
    if 0 in numbers:
        return False
    if len(set(numbers)) != 9:
        return False
    return True

def valid_solution(board):
    # check the rows
    for i in range(9):
        if not check_valid_numbers(board[i]):
            return False
        
    # check the columns
    for i in range(9):
        numbers = [row[i] for row in board]
        if not check_valid_numbers(numbers):
            return False
        
    # check the squares
    for i in range(3):
        for j in range(3):
            numbers = ([row[3*j:3*(j+1)] for row in board[3*i:3*(i+1)]])
            numbers = sum(numbers, [])
            if not check_valid_numbers(numbers):
                return False
    return True


'''
New solution refactored
'''
def check_valid_numbers(numbers):
    # set reorders the number, removes duplicates and checks length
    return set(numbers) == set(range(1,10))

def valid_solution(board):
    
    print(board)
    # check the rows
    for row in board:
        if not check_valid_numbers(row):
            return False

    # check the columns
    # transpose the board to check the columns
    transposed = zip(*board)
    for column in transposed:
        if not check_valid_numbers(column):
            return False

    # check the squares (3 x 3)
    for a in (0, 3, 6):
        for b in (0, 3, 6):
            numbers = []
            # get the numbers in the squares
            for i in (0,1,2):
                for j in (0,1,2):
                    numbers.append(board[a+i][b+j])
            if not check_valid_numbers(numbers):
                return False
    return True

if __name__ == "__main__":
    import codewars_test as test
    try:
        valid_solution = validSolution
    except NameError:
        pass

    test.assert_equals(valid_solution([
    [1, 3, 2, 5, 7, 9, 4, 6, 8], 
    [4, 9, 8, 2, 6, 1, 3, 7, 5], 
    [7, 5, 6, 3, 8, 4, 2, 1, 9], 
    [6, 4, 3, 1, 5, 8, 7, 9, 2], 
    [5, 2, 1, 7, 9, 3, 8, 4, 6], 
    [9, 8, 7, 4, 2, 6, 5, 3, 1], 
    [2, 1, 4, 9, 3, 5, 6, 8, 7], 
    [3, 6, 5, 8, 1, 7, 9, 2, 4], 
    [8, 7, 9, 6, 4, 2, 1, 3, 5]]), False);

    # test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
    #                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
    #                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
    #                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
    #                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
    #                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);