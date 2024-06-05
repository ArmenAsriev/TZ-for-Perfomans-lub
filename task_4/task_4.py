import sys


def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        nums = [int(line.strip()) for line in file]
    result = min_moves_to_equal_elements(nums)
    print(result)
