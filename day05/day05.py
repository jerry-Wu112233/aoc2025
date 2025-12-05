from dataclasses import dataclass
from bisect import bisect_right


@dataclass
class Interval:
    start: int
    end: int


def part1() -> int:
    intervals, ids = parse_input()
    count = 0
    starts = [iv.start for iv in intervals]

    for id in ids:
        i = bisect_right(starts, id) - 1
        if i >= 0:
            iv = intervals[i]
            if iv.start <= id <= iv.end:
                count += 1
    return count


def part2() -> int:
    intervals, _ = parse_input()

    unique_periods = 0
    for interval in intervals:
        unique_periods += interval.end - interval.start + 1
    return unique_periods


def parse_input() -> tuple[list[Interval], list[int]]:
    intervals: list[Interval] = []
    ids_to_check: list[int] = []

    with open("day05/input.txt", "r") as f:
        interval_data, id_data = f.read().strip().split("\n\n")
        for interval in interval_data.split("\n"):
            if not interval:
                continue

            start, end = interval.split("-")
            intervals.append(Interval(int(start), int(end)))
        for id in id_data.split("\n"):
            if not id:
                continue

            ids_to_check.append(int(id))
    return merge_intervals(intervals), ids_to_check


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    intervals.sort(key=lambda x: x.start)
    merged_intervals = [intervals[0]]
    for interval in intervals:
        current_interval = merged_intervals[-1]
        if current_interval.start <= interval.start <= current_interval.end:
            current_interval.end = max(current_interval.end, interval.end)
            continue
        merged_intervals.append(interval)
    return merged_intervals
