from itertools import chain, count
from pathlib import Path

root = Path(__file__).parent
validate = (root / "input.txt").read_text()
example = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
""".strip().replace("\n", "")


def parse(raw: str):
    yield from (x.split("-") for x in raw.split(","))


def part1(data: str):
    def invalidator(start: str, stop: str):
        """Check for invalid product ids in the given range."""
        for c in count(int(start[: len(start) // 2] or 0)):
            invalid_id = int(str(c) * 2)
            if invalid_id > int(stop):
                break
            if invalid_id >= int(start):
                yield invalid_id

    return sum(chain.from_iterable(invalidator(*d) for d in parse(data)))


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(data: str):
    def invalidator(start: str, stop: str):
        """Check for invalid product ids in the given range."""
        for m in range(2, len(stop) + 1):
            for c in count(int(start[: len(start) // m] or 0)):
                invalid_id = int(str(c) * m)
                if invalid_id > int(stop):
                    break
                if invalid_id >= int(start):
                    yield invalid_id

    return sum(chain.from_iterable(set(invalidator(*d)) for d in parse(data)))


print("part2: ", part2(example))
print("part2: ", part2(validate))
