def produce(n, board, r, c, new_stack):
    if r >= 1 and board[r - 1][c] == 0:
        board[r - 1][c] = board[r][c]
        new_stack.append((r - 1, c))
    if r < n - 1 and board[r + 1][c] == 0:
        board[r + 1][c] = board[r][c]
        new_stack.append((r + 1, c))
    if c >= 1 and board[r][c - 1] == 0:
        board[r][c - 1] = board[r][c]
        new_stack.append((r, c - 1))
    if c < n - 1 and board[r][c + 1] == 0:
        board[r][c + 1] = board[r][c]
        new_stack.append((r, c + 1))


def main():
    n, k = map(lambda x: int(x), input().split())

    stacks = [None]
    for _ in range(k):
        stacks.append([])

    board = []
    for r in range(n):
        board.append(list(map(lambda x: int(x), input().split())))
        for c in range(n):
            if board[r][c] != 0:
                stacks[board[r][c]].append((r, c))

    s, x, y = map(lambda a: int(a), input().split())

    for _ in range(s):
        for virus in range(1, k + 1):
            new_stack = []
            while len(stacks[virus]) > 0:
                r, c = stacks[virus].pop()
                produce(n, board, r, c, new_stack)
            stacks[virus] = new_stack

    print(board[x - 1][y - 1])


if __name__ == "__main__":
    main()
