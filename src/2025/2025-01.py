from pathlib import Path

root = Path(__file__).parent
validation = (root / "input.txt").read_text()
example = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()


def part1(raw: str):
    table = str.maketrans({"L": "-", "R": ""})
    data = map(int, raw.translate(table).split())

    current = 50
    for d in data:
        current = (current + d) % 100
        yield not current


print("part1", sum(part1(example)), sum(part1(validation)), sep="\n")


def part2(raw: str):
    table = str.maketrans({"L": "-", "R": ""})
    data = map(int, raw.strip().translate(table).split())

    position, MOD = 50, 100
    for n in data:
        if n > 0:
            overshoot = n + position - MOD
        elif position:
            overshoot = -n - position
        else:  # 0 compensation
            overshoot = -n - MOD
        position = (position + n) % MOD
        yield 1 + overshoot // MOD if overshoot >= 0 else 0


print("part2", sum(part2(example)), sum(part2(validation)), sep="\n")
