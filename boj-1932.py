def main():
    n = int(input())

    prev_floor = [int(input())]
    for width in range(2, n + 1):
        floor = list(map(lambda x: int(x), input().split()))
        floor[0] += prev_floor[0]
        for index in range(1, width - 1):
            floor[index] += max(prev_floor[index - 1], prev_floor[index])
        floor[-1] += prev_floor[-1]
        prev_floor = floor

    print(max(prev_floor))


if __name__ == "__main__":
    main()
