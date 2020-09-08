def main():
    n = int(input())
    m = int(input())

    costs = []
    for i in range(n):
        costs.append([1_000_000_000] * n)
        costs[i][i] = 0

    for _ in range(m):
        src, dst, cost = map(lambda x: int(x), input().split())
        costs[src - 1][dst - 1] = min(costs[src - 1][dst - 1], cost)

    for middle in range(n):
        for src in range(n):
            for dst in range(n):
                costs[src][dst] = min(costs[src][dst], costs[src][middle] + costs[middle][dst])

    answers = []
    for src in range(n):
        for dst in range(n):
            if costs[src][dst] >= 1_000_000_000:
                costs[src][dst] = '0'
            else:
                costs[src][dst] = str(costs[src][dst])
        answers.append(' '.join(costs[src]))
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
