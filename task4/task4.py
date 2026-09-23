import sys

MAX_MOVES = 20


def min_moves(nums):
    nums = sorted(nums)
    median = nums[len(nums) // 2]
    return sum(abs(x - median) for x in nums)


def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        nums = [int(token) for token in f.read().split()]
    moves = min_moves(nums)
    if moves <= MAX_MOVES:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


if __name__ == "__main__":
    main()