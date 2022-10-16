board = [[3,0,0,8,0,1,0,0,2],
         [2,0,1,0,3,0,6,0,4],
         [0,0,0,2,0,4,0,0,0],
         [8,0,9,0,0,0,1,0,6],
         [0,6,0,0,0,0,0,5,0],
         [7,0,2,0,0,0,4,0,9],
         [0,0,0,5,0,9,0,0,0],
         [9,0,4,0,8,0,7,0,5],
         [6,0,0,1,0,7,0,0,3]]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("–––––––––––––––––––––")
        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=" ")

# bo = board of sudoku puzzle
# number = number willing to test if valid
# position = [x-coord, y-coord] of point


def valid(bo, number, position):
    return row_valid(bo, number, position) and col_valid(bo, number, position) and box_valid(bo, number, position)


def row_valid(bo, number, position):
    row = position[1]
    for i in range(len(bo[row])):
        if bo[row][i] == number:
            return False
    return True


def col_valid(bo, number, position):
    col = position[0]
    for i in range(len(bo)):
        if bo[i][col] == number:
            return False
    return True


def box_valid(bo, number, position):
    x_box = position[0] // 3
    y_box = position[1] // 3
    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if bo[i][j] == number:
                return False
    return True


def empty_space(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return [j, i]
    return None


def solver(bo):
    find = empty_space(bo)
    if not find:
        print_board(bo)
        return True

    x, y = find
    for num in range(1, 10):
        if valid(bo, num, [x, y]):
            bo[y][x] = num
            if solver(bo):
                return True
            bo[y][x] = 0
    return False


print(solver(board))
