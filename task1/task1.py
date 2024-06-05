import sys


def circular_path(n, m):
    result = []
    i = 1
    while True:
        result.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = circular_path(n, m)
    print(''.join(map(str, path)))
