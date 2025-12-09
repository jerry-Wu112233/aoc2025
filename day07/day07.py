from collections import Counter, deque


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


def part1() -> tuple[int, int]:
    start, grid, depth = parse_input()
    queue = [(start, 1)]
    paths_at_each_coord = Counter()
    unique_paths = 0
    while queue:
        possible_paths = set()
        for _ in range(len(queue)):
            curr_pos, paths = queue.pop()
            if curr_pos.real == depth:
                unique_paths += paths
                continue
            paths_at_each_coord[curr_pos] += 1
            next_pos = curr_pos + complex(1, 0)
            if next_pos == "^":
                possible_paths.add(curr_pos + complex(1, -1))
                possible_paths.add(curr_pos + complex(1, 1))
            else:
                possible_paths.add(curr_pos + complex(1, 0))
        queue.append((coord, paths_at_each_coord[curr_pos]) for coord in possible_paths)
        paths_at_each_coord = Counter()

    return len(splitters_visited), path


print(part1())
