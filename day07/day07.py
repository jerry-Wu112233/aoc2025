from collections import Counter


def parse_input():
    grid = {}
    start = None
    with open("day07/input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, c in enumerate(line):
                grid[complex(i, j)] = c
                if c == "S":
                    start = complex(i, j)
            depth = i
    return start, grid, depth


def part_1_and_2() -> tuple[int, int]:
    start, grid, depth = parse_input()
    layer = [(start, 1)]
    paths_at_each_coord = Counter()
    unique_paths = 0
    splitters_visited = 0
    while layer:
        next_layer = []
        for _ in range(len(layer)):
            curr_pos, paths = layer.pop()

            if curr_pos.real == depth:
                unique_paths += paths
                continue

            paths_at_each_coord[curr_pos] += paths

        for curr_pos, paths in paths_at_each_coord.items():
            next_pos = curr_pos + complex(1, 0)
            if next_pos not in grid:
                continue
            if grid[next_pos] == "^":
                next_layer.append((curr_pos + complex(1, -1), paths))
                next_layer.append((curr_pos + complex(1, 1), paths))
                splitters_visited += 1
            else:
                next_layer.append((next_pos, paths))
        layer = next_layer
        paths_at_each_coord = Counter()
    return splitters_visited, unique_paths
