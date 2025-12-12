from pathlib import Path

from rich import print  # noqa: A004

validate = Path(__file__).with_suffix(".txt").read_text().strip()
example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def parse(raw: str):
    __ranges, _ingredients = raw.split("\n\n")
    _ranges = (x.split("-") for x in __ranges.split("\n"))
    ranges = [(int(x), int(y)) for x, y in _ranges]
    ingredients = [int(x) for x in _ingredients.split("\n")]
    return ranges, ingredients


def part1(raw: str):
    (ranges, ingredients) = parse(raw)
    return sum(any(s <= i <= e for s, e in ranges) for i in ingredients)


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    accumulate, (ranges, _) = 0, parse(raw)
    it = iter(sorted(ranges, key=lambda x: x[0]))
    start, stop = next(it)
    for s, e in it:
        if start <= s <= stop:
            stop = max(e, stop)
        else:
            accumulate += stop - start + 1
            start, stop = s, e
    accumulate += stop - start + 1

    return accumulate


print("part2: ", part2(example))
print("part2: ", part2(validate))
