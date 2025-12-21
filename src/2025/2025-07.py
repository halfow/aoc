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


def part1(raw: str):
    manifold = iter(raw.split()[::2])
    cnt, beams = 0, {next(manifold).index("S")}
    splitter_rows = [[i for i, c in enumerate(row) if c == "^"] for row in manifold]
    for splitters in splitter_rows:
        splits = beams.intersection(splitters)
        beams.difference_update(splits)
        beams.update(s + 1 for s in splits)
        beams.update(s - 1 for s in splits)
        cnt += len(splits)
    return cnt


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    manifold = iter(raw.split()[::2])
    paths = [int(c == "S") for c in next(manifold)]
    splitters = [i for row in manifold for i, c in enumerate(row) if c == "^"]
    for s in splitters:
        paths[s - 1] += paths[s]
        paths[s + 1] += paths[s]
        paths[s] = 0
    return sum(paths)


print("part2: ", part2(example))
print("part2: ", part2(validate))
