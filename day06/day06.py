import math
import numpy as np

def parse_input() -> tuple[list[str], list[str]]:
    number_list = []
    symbol_list = []

    with open("day06/input.txt") as f:
        *number_list, symbol_list = f.read().split("\n") 
        
    return number_list, symbol_list


def part1() -> int:
    nums, symbols, _ = parse_input()
    nums_arr = []
    for num_list in nums:
        nums_arr.append([int(x) for x in num_list.strip().split()])
    nums_arr = np.array(nums_arr)
    symbols = symbols.strip().split()
    result = 0
    for num_list, sym in zip(nums_arr.T, symbols):
        if sym == "*":
            result += math.prod(num_list)
        else:
            result += sum(num_list)
    return result

def part2() -> int:
    nums, syms = parse_input()
    total = 0
    column = len(nums[0]) - 1
    numbers = []
    while column >= 0:
        while True:
            numbers.append(int(''.join([line[column] for line in nums])))
            if syms[column] == ' ': 
                column -= 1
            else:
                if syms[column] == "+":
                    total += sum(numbers)
                else:
                    total += math.prod(numbers)
                numbers = []
                column -= 2
                break
    return total