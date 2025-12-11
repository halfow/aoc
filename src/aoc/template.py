from pathlib import Path

validate = Path(__file__).with_suffix(".txt").read_text().strip()
example = """
"""


def parse(raw: str):
    pass


def part1(raw: str):
    return


print("part1: ", part1(example))
# print("part1: ", part1(validate))


def part2(raw: str):
    return


print("part2: ", part2(example))
# print("part2: ", part2(validate))
