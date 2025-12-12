from collections import Counter
from collections.abc import Generator
from itertools import product
from pathlib import Path

from rich import print  # noqa: A004

validate = Path(__file__).with_suffix(".txt").read_text().strip()
example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()


class Grid(list):
    def __init__(self, raw: str):
        super().__init__(list(line) for line in raw.split("\n"))

    def __iter__(self) -> Generator[tuple[tuple[int, int], str]]:
        for x, y in product(
            range(len(self[0])),
            range(len(self)),
        ):
            yield (x, y), self[y][x]

    def kernel(self, x: int, y: int, k: int):
        for a, b in product(
            range(max(x - k, 0), min(x + k + 1, len(self[0]))),
            range(max(y - k, 0), min(y + k + 1, len(self))),
        ):
            yield self[b][a]


def part1(raw: str):
    grid, result = Grid(raw), 0
    for pos, char in grid:
        if char == "@":
            result += Counter(grid.kernel(*pos, 1))["@"] < 5
    return result


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    grid, result = Grid(raw), 0
    while True:
        rm = []
        for pos, char in grid:
            if (char == "@") and (Counter(grid.kernel(*pos, 1))["@"] < 5):
                result += 1
                rm.append(pos)

        if not rm:
            break

        while rm:
            x, y = rm.pop()
            grid[y][x] = "."

    return result


print("part2: ", part2(example))
print("part2: ", part2(validate))
