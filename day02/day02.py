def parse_input() -> list[tuple[int, int]]:
    results = []
    with open("day02/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            entries = line.split(",")
            for entry in entries:
                if not entry:
                    continue
                nums = entry.split("-")
                results.append((int(nums[0]), int(nums[1])))

    return results


def part1() -> int:
    res = 0
    for start, end in parse_input():
        for id in range(start, end + 1):
            res += id if id_contains_duplicates(id) else 0
    return res


def part2() -> int:
    res = 0
    for start, end in parse_input():
        for id in range(start, end + 1):
            res += id if string_partitions_are_equal(str(id)) else 0
    return res


def id_contains_duplicates(id: int) -> bool:
    id = str(id)
    return id[: len(id) // 2] == id[len(id) // 2 :]


def string_partitions_are_equal(s: str) -> bool:
    for k in range(1, len(s)):
        if len(s) % k == 0:
            partitions = partition_string(s, k)
            if len(set(partitions)) == 1:
                return True
    return False


def partition_string(s: str, k: int) -> list[str]:
    return [s[i : i + k] for i in range(0, len(s), k)]
