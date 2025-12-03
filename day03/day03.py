from itertools import combinations


def parse_input() -> list[str]:
    results = []
    with open("day03/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            results.append(line)
    return results


def part1() -> int:
    return sum(int(find_largest_num_to_form(n, 2)) for n in parse_input())


def part2() -> int:
    return sum(int(find_largest_num_to_form(n, 12)) for n in parse_input())


def find_largest_num_to_form(s: str, digits: int) -> str:
    assert digits <= len(s)
    if digits == 1:
        return max(s)

    idx = s.index(max(s[: len(s) - digits + 1]))
    return s[idx] + find_largest_num_to_form(s[idx + 1 :], digits - 1)
