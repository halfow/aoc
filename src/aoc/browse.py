from os import environ
from typing import Literal
from httpx import Client
import webbrowser

SESSION = environ.get("Session")


class AoC(Client):
    def __init__(self, year, day, session: str | None = SESSION, **kwargs) -> None:
        if session is None:
            raise ValueError("Session token not set")

        super().__init__(base_url="https://adventofcode.com", cookies={"session": session}, **kwargs)
        self.year = year
        self.day = day

    def fetch(self):
        return self.get(f"{self.year}/day/{self.day}/input")

    def submit(self, part: Literal[1, 2], answer):
        print(self.post(f"{self.year}/day/{self.day}/answer", data={"level": part, "answer": answer}).text)

    def browser(self):
        webbrowser.open(f"{self.base_url}/{self.year}/day/{self.day}")
