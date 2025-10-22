from pathlib import*


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open("./input.txt")