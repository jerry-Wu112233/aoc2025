import itertools
from typing import Union
from shapely import Polygon, LineString


def parse_input() -> list[tuple[int, int]]:
    coords = []
    with open("day08/input.txt") as f:
        for line in f.readlines():
            i, j = line.split(",")
            coords.append((int(i), int(j)))
    return coords


def part1() -> int:
    coords = parse_input()
    max_area = 0
    for coord_1, coord_2 in itertools.combinations(coords, 2):
        max_area = max(max_area, get_area(coord_1, coord_2))
    return int(max_area)


def part2() -> int:
    coords = parse_input()
    polygon = Polygon(coords)
    max_area = 0
    for coord_1, coord_2 in itertools.combinations(coords, 2):
        shape = construct_rectangle_or_line_segment(coord_1, coord_2)
        if polygon.covers(shape):
            max_area = max(max_area, get_area(coord_1, coord_2))
    return max_area


def get_area(
    coord_1: tuple[int, int], coord_2: tuple[int, int]
) -> Union[LineString, Polygon]:
    return int((abs(coord_1[0] - coord_2[0]) + 1) * (abs(coord_1[1] - coord_2[1]) + 1))


def construct_rectangle_or_line_segment(
    coord_1: tuple[int, int], coord_2: tuple[int, int]
):
    if coord_1[0] == coord_2[0] or coord_1[1] == coord_2[1]:
        return LineString([coord_1, coord_2])
    left_most_coord = min(coord_1, coord_2)
    right_most_coord = max(coord_1, coord_2)
    """
    a   or   b
     a     b  
    """
    coord_to_constr1 = (right_most_coord[0], left_most_coord[1])
    coord_to_constr2 = (left_most_coord[0], right_most_coord[1])
    return Polygon(
        [left_most_coord, coord_to_constr1, right_most_coord, coord_to_constr2]
    )
