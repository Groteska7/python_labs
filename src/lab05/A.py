import json
from pathlib import Path
import csv
from src.lab05.lib import r_json, write_csv, r_csv, w_json

# path_json_samples = Path("data/lab05/samples/people.json")
# path_json_out = Path("data/lab05/out/people_from_json.csv")

# path_csv_samples = Path("data/lab05/samples/people.csv")
# path_csv_out = Path("data/lab05/out/people_from_csv.json")

# path_json = Path(input("Введите путь к json файлу: "))
# path_csv = Path(input("Введите путь к csv файлу: "))

def json_to_csv(json_path: str|Path, csv_path: str|Path) -> None:
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix != ".json":
        raise TypeError ("Неверный тип файла")
    if csv_path.suffix != ".csv":
        raise TypeError ("Неверный тип файла")
    if not json_path.exists():
        raise FileNotFoundError("json файл не найден")
    # if not csv_path.exists():
    #     raise FileNotFoundError("csv файл не найден")
    if json_path.stat().st_size ==0:
        raise ValueError("файл пуст")
    start=r_json(json_path)
    write_csv(start,csv_path)
    print("json_to_csv: Данные записаны")

def csv_to_json(csv_path: str|Path, json_path: str|Path) -> None:
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix != ".json":
        raise TypeError ("Неверный тип файла")
    if csv_path.suffix != ".csv":
        raise TypeError ("Неверный тип файла")
    if not csv_path.exists():
        raise FileNotFoundError("Файл не найден")
    if csv_path.stat().st_size ==0:
        raise ValueError("файл пуст")
    csv_file=r_csv(csv_path)
    w_json(csv_file,json_path)
    print("csv_to_json: Данные записаны")

# json_to_csv(path_json_samples,path_json_out)
# csv_to_json(path_csv_samples,path_csv_out) 