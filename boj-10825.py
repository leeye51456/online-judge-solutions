def main():
    n = int(input())

    scores = []
    for _ in range(n):
        name, korean, english, math = input().split()
        korean, english, math = map(lambda x: int(x), (korean, english, math))
        scores.append((-korean, english, -math, name))

    for name in map(lambda x: x[3], sorted(scores)):
        print(name)


if __name__ == "__main__":
    main()
