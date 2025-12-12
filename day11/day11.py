import networkx as nx

digraph = nx.DiGraph()
with open("day11/input.txt") as f:
    for line in f.readlines():
        source, routes = line.split(":")
        for dest in [route.strip() for route in routes.split()]:
            digraph.add_edge(source, dest)


def part1() -> int:
    return len(nx.all_simple_paths(digraph, "you", "out"))


def part2() -> int:
    return len(nx.all_simple_paths(digraph, "svr", "fft")) * len(nx.all_simple_paths(digraph, "fft", "dac")) * len(
        nx.all_simple_paths(digraph, "dac", "out")
    ) + len(nx.all_simple_paths(digraph, "svr", "dac")) * len(nx.all_simple_paths(digraph, "dac", "fft")) * len(
        nx.all_simple_paths(digraph, "fft", "out")
    )


print(part2())
