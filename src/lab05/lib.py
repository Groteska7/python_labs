import json
from pathlib import Path
import csv

def ensure_parent_dir(path: str | Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]

#---------------Чтение/запись json файлов---------------
path_json = Path("data/lab05/out/people.json")

def w_json(data: any, path: Path|str) -> None:
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != ".json" or path.stat().st_size ==0:
        raise ValueError("Неверный тип файла или файл пуст")
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def r_json(path: Path|str) -> any:
    if path.suffix != ".json" or path.stat().st_size ==0:
        raise ValueError("Неверный тип файла или файл пуст")
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

# print(r_json(path_json))

#---------------Чтение/запись csv файлов---------------
path_csv = Path("data/lab05/out/people.csv")

def write_csv(data: list[tuple | list], path: str | Path) -> None:
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != ".csv" or path.stat().st_size ==0:
        raise ValueError("Неверный тип файла или файл пуст")
    headers = list(data[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)#Записывает все кроме КЛЮЧАЙ в словарях, определяя ключи в этой строке под filednsmes
        writer.writeheader()
        writer.writerows(data)

def r_csv(path: Path|str) -> list:
    if path.suffix != ".csv" or path.stat().st_size ==0:
        raise ValueError("Неверный тип файла или файл пуст")
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    answ=[]
    with open(path, "r", encoding="utf-8") as file:
        read=csv.DictReader(file)
        for row in read:
            answ.append(row)
    return answ

# print(r_CSV(path_csv))


