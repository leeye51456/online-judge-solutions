import collections


def get_next_direction(direction, rotation):
    if (direction == 'r' and rotation == 'L') or (direction == 'l' and rotation == 'D'):
        return 'u'
    if (direction == 'd' and rotation == 'L') or (direction == 'u' and rotation == 'D'):
        return 'r'
    if (direction == 'l' and rotation == 'L') or (direction == 'r' and rotation == 'D'):
        return 'd'
    # if (direction == 'u' and rotation == 'L') or (direction == 'd' and rotation == 'D'):
    return 'l'

def get_next_position(head, direction):
    if direction == 'u':
        return (head[0] - 1, head[1])
    if direction == 'r':
        return (head[0], head[1] + 1)
    if direction == 'd':
        return (head[0] + 1, head[1])
    # if direction == 'l':
    return (head[0], head[1] - 1)

def is_valid_position(n, next_position):
    r, c = next_position
    return (0 <= r < n) and (0 <= c < n)


def simulate(n, board, rotations):
    direction = 'r'
    snake = collections.deque([(0, 0)])
    head = (0, 0)
    t = 0

    while True:
        t += 1

        head = get_next_position(head, direction)
        r, c = head

        if not is_valid_position(n, head) or board[r][c] == 's':
            return t
        snake.append(head)

        if board[r][c] != 'a':
            rt, ct = snake.popleft()
            board[rt][ct] = '.'
        board[r][c] = 's'

        if t in rotations:
            direction = get_next_direction(direction, rotations[t])


def main():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(['.'] * n)
    board[0][0] = 's'
    rotations = {}

    k = int(input())
    for _ in range(k):
        r, c = map(lambda x: int(x), input().split())
        board[r - 1][c - 1] = 'a'

    l = int(input())
    for _ in range(l):
        t, d = input().split()
        rotations[int(t)] = d

    print(simulate(n, board, rotations))


if __name__ == "__main__":
    main()
