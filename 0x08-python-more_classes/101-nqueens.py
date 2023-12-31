#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    def nset(qn=0):
        def is_safe(board, row, col):
            for i in range(col):
                if board[row][i] == 1:
                    return False

            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
                if board[i][j] == 1:
                    return False

            return True

        def solve_nqueens(board, col, qset):
            if col == len(board):
                qset.append([[i, j] for i in range(len(board))
                            for j in range(len(board)) if board[i][j] == 1])
                return

            for i in range(len(board)):
                if is_safe(board, i, col):
                    board[i][col] = 1
                    solve_nqueens(board, col + 1, qset)
                    board[i][col] = 0

        qset = []
        board = [[0 for _ in range(qn)] for _ in range(qn)]
        solve_nqueens(board, 0, qset)
        return qset

    def main():
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            qn = int(sys.argv[1])
        except Exception:
            print("N must be a number")
            sys.exit(1)

        if qn < 4:
            print("N must be at least 4")
            sys.exit(1)

        seted = nset(qn)
        for i in seted:
            print(i)

    main()
