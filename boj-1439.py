# https://www.acmicpc.net/problem/1439

def main():
    string = input()
    current = string[0]

    count = [0, 0]
    count[int(current)] += 1

    for char in string[1:]:
        if char != current:
            current = char
            count[int(current)] += 1

    print(min(count))


if __name__ == "__main__":
    main()
