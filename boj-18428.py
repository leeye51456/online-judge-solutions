n = 0
space = []
teachers = []


def scanned(teacher, coords):
    row, col = teacher
    for r in range(row - 1, -1, -1):
        if space[r][col] == 'S':
            return True
        if (r, col) in coords:
            break
    for r in range(row + 1, n):
        if space[r][col] == 'S':
            return True
        if (r, col) in coords:
            break
    for c in range(col - 1, -1, -1):
        if space[row][c] == 'S':
            return True
        if (row, c) in coords:
            break
    for c in range(col + 1, n):
        if space[row][c] == 'S':
            return True
        if (row, c) in coords:
            break
    return False


def can_avoid(coords):
    global n, space, teachers

    for teacher in teachers:
        if scanned(teacher, coords):
            return False
    return True


def pick(rest, row, col, coords):
    global n, space

    coords = [*coords, (row, col)]
    if rest == 0:
        return can_avoid(coords)

    for c in range(col + 1, n):
        if space[row][c] == 'X' and pick(rest - 1, row, c, coords):
            return True
    for r in range(row + 1, n):
        for c in range(n):
            if space[r][c] == 'X' and pick(rest - 1, r, c, coords):
                return True
    return False


def main():
    global n, space, teachers

    n = int(input())
    space = []
    teachers = []
    for r in range(n):
        space.append(input().split())
        for c in range(n):
            if space[r][c] == 'T':
                teachers.append([r, c])

    for r in range(n):
        for c in range(n):
            if space[r][c] == 'X' and pick(2, r, c, []):
                print('YES')
                return
    print('NO')


if __name__ == "__main__":
    main()
