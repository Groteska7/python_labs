from pathlib import Path
import sys
import csv
from collections import Counter
import os

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.lab03.text.tokenize import tokenize_f
from src.lab03.text.normalize import normalize_f



def ensure_parent_dir(path: str | Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True) #создаю родительские директории (Parents=True)/ НЕ вызываю ошибку при их отсуцтвии (exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path=Path(path)
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    try:
        with open(path,"r",newline="",encoding=encoding) as file:
            in_file=str(file.read())
        return normalize_f(in_file)
    except UnicodeDecodeError:
        print("неверная кодировка")


# print({Path.cwd()})
# for item in Path.cwd().iterdir():
#     print(f"  {item.name}")
# print(read_text(Path("data") / "input.txt"))

# def ensure_parent_dir(path: str | Path) -> None:
#     if 

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    path=Path(path)
    ensure_parent_dir(path)
    len_form=len(rows[0])
    for x in rows:
        if len_form!=len(x):
            raise ValueError("Ошибка чтения файла")
            break
    with open(path,"w",newline="",encoding="utf-8") as file:
        if header is not None:
            csv.writer(file,delimiter=",").writerow(header)
        csv.writer(file,delimiter=",").writerows(rows)
        print("файл создан/изменен")


def frequencies_from_text(text: str) -> dict[str, int]:
    if text==None:
        raise ValueError("неверный формат")
    tokens = tokenize_f(normalize_f(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
        
        