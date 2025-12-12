from argparse import ArgumentParser, Namespace
from os import environ
from pathlib import Path

from aoc.browse import AoC


class Parser(Namespace):
    year: int
    day: int
    session: str
    output: Path


def cli():
    parser = ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument(
        *("-s", "--session"),
        help="session token",
        default=environ.get("SESSION"),
        required=not bool(environ.get("SESSION")),
    )
    parser.add_argument(
        *("-o", "--output"),
        type=Path,
        default=Path.cwd() / "src",
    )

    args = parser.parse_args(namespace=Parser())
    aoc = AoC(args.year, args.day, args.session)
    day = args.output / str(args.year) / f"{args.year}-{args.day:02}"

    validation = day.with_suffix(".txt")
    if not validation.exists():
        response = aoc.validation_set()
        validation.write_text(response.text)

    solution = day.with_suffix(".py")
    if not solution.exists():
        solution.write_text(Path(__file__).with_name("template.py").read_text())

    aoc.browser()


if __name__ == "__main__":
    raise SystemExit(cli())
