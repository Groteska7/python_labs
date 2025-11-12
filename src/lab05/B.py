from openpyxl import Workbook
from pathlib import Path
import csv
from lib import r_json, r_csv


path_csv_samples = Path("data/lab05/samples/cities.csv")
xlsx_path = Path("data/lab05/out/people.xlsx")


def csv_to_xlsx(csv_path: str|Path, xlsx_path: str|Path) -> None:
    csv_data=r_csv(csv_path)
    # print(csv_data)

    mas=[]
    lis=[]
    for key in csv_data[0].keys():
        lis.append(str(key))
    mas.append(lis)
    # print(mas)
    lis=[]
    for row in csv_data:
        for key in csv_data[0].keys():
            lis.append(row[key])
        mas.append(lis)
        lis=[]
    with open(csv_path, encoding="utf-8") as file:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        for row in mas:
            ws.append(row)
        wb.save(xlsx_path)

csv_to_xlsx(path_csv_samples,xlsx_path)