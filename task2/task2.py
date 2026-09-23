import sys
from fractions import Fraction


def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [Fraction(token.replace(",", ".")) for token in f.read().split()]


def position(x, y, cx, cy, rx, ry):
    value = (x - cx) ** 2 / rx ** 2 + (y - cy) ** 2 / ry ** 2
    if value == 1:
        return 0
    if value < 1:
        return 1
    return 2


def main():
    cx, cy, rx, ry = read_numbers(sys.argv[1])
    coords = read_numbers(sys.argv[2])
    for i in range(0, len(coords) - 1, 2):
        print(position(coords[i], coords[i + 1], cx, cy, rx, ry))


if __name__ == "__main__":
    main()