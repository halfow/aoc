from os import environ
from pathlib import Path

from aoc.browse import AoC
from argparse import ArgumentParser, Namespace


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

    data = day.with_suffix(".txt")
    if not data.exists():
        response = aoc.fetch()
        data.write_text(response.text)

    template = day.with_suffix(".py")
    if not template.exists():
        template.write_text(Path(__file__).with_name("template.py").read_text())

    aoc.browser()
