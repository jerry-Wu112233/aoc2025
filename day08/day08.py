import heapq
from itertools import combinations
import math


class DisjointSetUnion:
    def __init__(self, elements):
        self.parent = {}
        self.size = {}
        for element in elements:
            self.parent[element] = element
            self.size[element] = 1

    def find(self, element):
        if self.parent[element] == element:
            return element
        self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1

            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def get_all_set_sizes(self):
        valid_sizes = []
        for element in self.parent:
            if self.parent[element] == element:
                valid_sizes.append(self.size[element])
        return valid_sizes

    def get_set_count(self):
        count = 0
        for element in self.parent:
            if self.parent[element] == element:
                count += 1
        return count


def parse_input() -> list[tuple[int]]:
    coords = []
    with open("day08/input.txt") as f:
        for line in f.readlines():
            coords.append(tuple(map(int, line.split(","))))
    return coords


def euc_dist(coord_1: tuple[int], coord_2: tuple[int]) -> float:
    return math.sqrt((coord_1[0] - coord_2[0]) ** 2 + (coord_1[1] - coord_2[1]) ** 2 + (coord_1[2] - coord_2[2]) ** 2)


def part1_and_2() -> int:
    coords = parse_input()
    disjoint_set = DisjointSetUnion(coords)
    coord_dists = []
    for coord_1, coord_2 in combinations(coords, 2):
        coord_dists.append((euc_dist(coord_1, coord_2), coord_1, coord_2))
    coord_dists.sort(key=lambda x: x[0])
    iterations = 0
    coord_prod = 0
    largest_union_prod = 0
    for _, coord_1, coord_2 in coord_dists:
        iterations += 1
        disjoint_set.union(coord_1, coord_2)
        if disjoint_set.get_set_count() == 1:
            coord_prod = coord_1[0] * coord_2[0]
            break
        if iterations == 1000:
            largest_union_prod = math.prod(heapq.nlargest(3, disjoint_set.get_all_set_sizes()))

    return largest_union_prod, coord_prod
