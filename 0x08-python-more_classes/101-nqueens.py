import sys


def checkPos(board, pos):
    for x in range(pos[0]):
        if board[x][pos[1]] == 1:
            return False

    for x, y in zip(range(pos[0], -1, -1), range(pos[1], -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(pos[0], -1, -1), range(pos[1], len(board), 1)):
        if board[x][y] == 1:
            return False

    return True


def nqueens(board, row, solutions):
    if row == len(board):
        solutions.append(conv(board))
        #solutions.append([x[:] for x in board])

    for x in range(len(board)):
        if checkPos(board, (row, x)) == True:
            board[row][x] = 1
            nqueens(board, row + 1, solutions)
            board[row][x] = 0

def conv(sol):
    fin = []
    for x in range(len(sol)):
        fin.append([])
        fin[x].append(x)
        for y in range(len(sol)):
            if sol[x][y] == 1:
                fin[x].append(y)
                break
    return fin

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    num = int(sys.argv[1])
    board = [[0] * num for x in range(num)]
    sols = []
    nqueens(board, 0, sols)
    for x in sols:
        print(x)

if __name__ == "__main__":
    main()
