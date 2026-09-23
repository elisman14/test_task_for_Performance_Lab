import sys


def circular_path(n, m):
    path = []
    start = 1
    while True:
        path.append(start)
        end = (start - 1 + m - 1) % n + 1
        if end == 1:
            break
        start = end
    return path


def main():
    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    result = circular_path(n1, m1) + circular_path(n2, m2)
    print("".join(map(str, result)))


if __name__ == "__main__":
    main()