def part_1():
    with open("day12/input.txt") as f:
        *_, tree_requirements = f.read().strip().split("\n\n")
        count = 0
        for tree in tree_requirements.split("\n"):
            dimension, requirement = tree.split(":")
            width, height = map(int, dimension.split("x"))
            count += int(width // 3 * height // 3) >= sum(map(int, requirement.split()))
        return count
