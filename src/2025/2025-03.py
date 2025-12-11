from pathlib import Path

root = Path(__file__).parent
validate = (root / "input.txt").read_text().strip()
example = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()


def parse(raw: str):
    yield from (list(map(int, line)) for line in raw.split("\n"))


def max_jolt(battery_bank: list[int], n=12):
    optimal, start = [], 0
    for stop in range(1 - n, 1):
        search_range = battery_bank[start : stop or None]
        optimal.append(max(search_range))
        start = search_range.index(optimal[-1]) + start + 1
    return int("".join(map(str, optimal)))


def part1(raw: str):
    return sum(max_jolt(bank, 2) for bank in parse(raw))


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    return sum(max_jolt(bank, 12) for bank in parse(raw))


print("part2: ", part2(example))
print("part2: ", part2(validate))
