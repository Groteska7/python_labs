import argparse
from pathlib import Path
from src.lab05.A import json_to_csv, csv_to_json
from src.lab05.B import csv_to_xlsx
from lib import make_obs

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd") # по умолчанию активируется при запуске кода. Прописывать не нужно

    p1 = sub.add_parser("json2csv",help="конвертация lson to csv") # Необходимо прописыват ьпосле импорта файла
    p1.add_argument("-i", "--input", dest="input_file", help="Входной файл .json", required=True,type=str)
    p1.add_argument("-o", "--output", dest="output_file", help="конечный файл .csv", required=True,type=str)

    p2 = sub.add_parser("csv2json",help="конвертация csv to json")# Необходимо прописыват ьпосле импорта файла
    p2.add_argument("-i", "--input", dest="input_file", help="входной файл .csv", required=True,type=str)
    p2.add_argument("-o", "--output", dest="output_file", help="конечный файл .json", required=True,type=str)

    p3 = sub.add_parser("csv2xlsx",help="конвертация csv to xlsx")# Необходимо прописыват ьпосле импорта файла
    p3.add_argument("-i", "--input", dest="input_file", help="входной файл .csv", required=True,type=str)
    p3.add_argument("-o", "--output", dest="output_file", help="конечный файл xlsx", required=True,type=str)

    args = parser.parse_args()

    
    
    if not make_obs(args.input_file).is_file():
        parser.error(f"Указанный путь {args.output_file} не является файлом")


    if args.cmd == "json2csv":
        json_to_csv(make_obs(args.input_file),make_obs(args.output_file))
    
    if args.cmd == "csv2json":
        csv_to_json(make_obs(args.input_file),make_obs(args.output_file))
    
    if args.cmd == "csv2xlsx":
        csv_to_xlsx(make_obs(args.input_file),make_obs(args.output_file))



if __name__ == "__main__":
    main()
