import operator
import re
from functools import reduce
from pathlib import Path

from rich import print  # noqa: A004

validate = Path(__file__).with_suffix(".txt").read_text().strip("\n")
example = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip("\n")  # noqa: W291


def part1(raw: str):
    PATTERN = re.compile(r"(\S+)\s*")
    op = {"+": operator.add, "*": operator.mul}
    data = zip(*(PATTERN.findall(i) for i in raw.split("\n")), strict=True)
    return sum(reduce(op[o], map(int, i)) for *i, o in data)


print("part1: ", part1(example))
print("part1: ", part1(validate))


def part2(raw: str):
    *lines, ops = raw.split("\n")
    PATTERN = re.compile(r"(?P<op>[+*])\s*")
    starts = list(PATTERN.finditer(ops))
    op = {"+": operator.add, "*": operator.mul}

    for match in starts:
        k = []
        for i in range(match.start(), match.end()):
            if n := "".join(line[i] for line in lines).strip():
                k.append(int(n))  # noqa: PERF401
        yield reduce(op[match["op"]], k)


print("part2: ", sum(part2(example)))
print("part2: ", sum(part2(validate)))
