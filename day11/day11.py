import functools
import networkx as nx

digraph = nx.DiGraph()
with open("day11/input.txt") as f:
    for line in f.readlines():
        source, routes = line.split(":")
        for dest in [route.strip() for route in routes.split()]:
            digraph.add_edge(source, dest)


def part1() -> int:
    return sum(1 for _ in nx.all_simple_paths(digraph, "you", "out"))


def part2() -> int:
    START = "svr"
    FFT = "fft"
    DAC = "dac"
    END = "out"
    return count_paths(START, FFT) * count_paths(FFT, DAC) * count_paths(DAC, END) + count_paths(
        START, DAC
    ) * count_paths(DAC, FFT) * count_paths(FFT, END)


def count_paths(start: str, end: str) -> int:
    @functools.cache
    def dfs_cached(current_node):
        if current_node == end:
            return 1
        count = 0
        try:
            for v in digraph.successors(current_node):
                count += dfs_cached(v)
        except nx.exception.NetworkXError:
            return 0
        return count

    return dfs_cached(start)
