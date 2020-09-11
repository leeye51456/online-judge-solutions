memo = {}
n = 0
t = []
p = []


def get_price_max(begin):
    global memo, n, t, p

    if begin >= n:
        return 0

    if begin in memo:
        return memo[begin]

    maximum = 0
    for index in range(begin, n):
        if index + t[index] <= n:
            current = p[index] + get_price_max(index + t[index])
            if current > maximum:
                maximum = current

    memo[begin] = maximum
    return maximum


def main():
    global n, t, p

    n = int(input())
    for day in range(n):
        ti, pi = map(lambda x: int(x), input().split())
        t.append(ti)
        p.append(pi)

    print(get_price_max(0))


if __name__ == "__main__":
    main()
