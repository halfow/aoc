from pathlib import Path

from rich import print  # noqa: A004

validate = Path(__file__).with_suffix(".txt").read_text().strip()
example = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()


def parse(raw: str) -> list[str]:
    return raw.split()[::2]


parse(example)


def part1(raw: str):
    manifold = iter(parse(raw))
    splits, beams = 0, {next(manifold).index("S")}
    for i in manifold:
        emission: set[int] = set()
        for b in beams:
            if i[b] == "^":
                splits += 1
                emission.update((b + 1, b - 1))
            else:
                emission.add(b)
        beams = emission
    return splits


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    manifold = iter(parse(raw))
    paths = [int(c == "S") for c in next(manifold)]
    splitters = [i for row in manifold for i, c in enumerate(row) if c == "^"]
    for s in splitters:
        paths[s - 1] += paths[s]
        paths[s + 1] += paths[s]
        paths[s] = 0
    return sum(paths)


print("part2: ", part2(example))
print("part2: ", part2(validate))
