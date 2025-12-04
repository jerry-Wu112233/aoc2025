from collections import deque
from itertools import product
from typing import Iterator

grid = {}

directions = set(product((1, 0, -1), (1, 0, -1))) - {(0, 0)}
with open("day04/input.txt", "r") as f:
    for row, line in enumerate(f):
        line = line.strip()
        if not line:
            continue
        for col, c in enumerate(line):
            grid[row + col * 1j] = c


def part1() -> int:
    return sum(1 if check_neighbors(coord) else 0 for coord in grid)


def part2() -> int:
    queue = deque()

    removed = 0
    for coord in grid:
        if check_neighbors(coord):
            removed += 1
            grid[coord] = "."
            for neighbor in get_neighboring_coords(coord):
                queue.append(neighbor)

    while queue:
        for _ in range(len(queue)):
            curr_coord = queue.popleft()
            if not check_neighbors(curr_coord):
                continue

            removed += 1
            grid[curr_coord] = "."
            for neighbor in get_neighboring_coords(curr_coord):
                queue.append(neighbor)
    return removed


def get_neighboring_coords(coord: complex) -> Iterator[complex]:
    for x_dir, y_dir in directions:
        coord_to_check = coord + (x_dir + y_dir * 1j)
        if coord_to_check not in grid:
            continue
        if grid[coord_to_check] == ".":
            continue
        yield coord_to_check


def check_neighbors(coordinate: complex) -> bool:
    if grid[coordinate] == ".":
        return False
    neighbors = 0
    for coord_to_check in get_neighboring_coords(coordinate):
        neighbors += 1 if grid[coord_to_check] == "@" else 0
    return neighbors < 4
