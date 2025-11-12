import json
from pathlib import Path
import csv
from lib import r_json, write_csv, r_csv, w_json

path_json_samples = Path("data/lab05/samples/people.json")
path_json_out = Path("data/lab05/out/people_from_json.csv")

path_csv_samples = Path("data/lab05/samples/people.csv")
path_csv_out = Path("data/lab05/out/people_from_csv.json")

# path_json = Path(input("Введите путь к json файлу: "))
# path_csv = Path(input("Введите путь к csv файлу: "))

def json_to_csv(json_path: str|Path, csv_path: str|Path) -> None:
    if not json_path.exists() or not csv_path.exists():
        raise FileNotFoundError("Файл не найден")
    if json_path.suffix != ".json" or json_path.stat().st_size ==0 or csv_path.suffix != ".csv":
        raise ValueError("Неверный тип файла или файл пуст")
    start=r_json(json_path)
    write_csv(start,csv_path)
    print("json_to_csv: Данные записаны")

def csv_to_json(csv_path: str|Path, json_path: str|Path) -> None:
    if not json_path.exists() or not csv_path.exists():
        raise FileNotFoundError("Файл не найден")
    if json_path.suffix != ".json" or csv_path.suffix != ".csv" or csv_path.stat().st_size ==0:
        raise ValueError("Неверный тип файла или файл пуст")
    csv_file=r_csv(csv_path)
    w_json(csv_file,json_path)
    print("csv_to_json: Данные записаны")

json_to_csv(path_json_samples,path_json_out)
csv_to_json(path_csv_samples,path_csv_out) 