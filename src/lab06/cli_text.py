
import argparse
import sys
from pathlib import Path
from lib import make_obs

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.lab05.lib import r_csv, r_json
from src.lab03.text.count_freq import top_n, count_freq_f
from src.lab03.text.tokenize import tokenize_f

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("-i", "--input", dest="input_file", required=True, help="Путь входного файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("-i", "--input", dest="input_file", required=True, help="Путь входного файла")
    stats_parser.add_argument("--top", dest="top_n", type=int, default=5, help="вывести топ-X слов по частоте")

    args = parser.parse_args()

    path=Path(args.input_file)
    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if not path.is_file():
        parser.error(f"Указанный путь {args.input_file} не является файлом")
    
    if args.command == "cat":
        if not path.exists():
            raise FileNotFoundError("Указанный файл не найден")
        if path.suffix==".csv":
            data=list(list(x.values()) for x in r_csv(path))
        elif path.suffix==".json":
            data=data=list(list(x.values()) for x in r_json(path))
        elif path.suffix==".txt":
            with open(path,"r",encoding="utf-8") as file:
                data = tokenize_f(file.read())
                print(data)
            if args.n:
                for i in range(len(data)):
                    print(i+1,data[i])
            else:
                for i in range(len(data)):
                    print(data[i])
            sys.exit()
        else:
            raise ValueError("Недопустимый формат файла")
        
        if args.n:
            for i in range(len(data)):
                print(i+1,", ".join(data[i]))
        else:
            for i in range(len(data)):
                print(", ".join(data[i]))


    elif args.command == "stats":
        if not path.exists():
            raise FileNotFoundError("Указанный файл не найден")

        if path.suffix==".csv":
            data=list(list(x.values()) for x in r_csv(path))
        elif path.suffix==".json":
            data=data=list(list(x.values()) for x in r_json(path))
        elif path.suffix==".txt":
            with open(path,"r",encoding="utf-8") as file:
                data = file.read()
        else:
            raise ValueError("Недопустимый формат файла")

        data=top_n(count_freq_f(tokenize_f(data)),args.top_n)
        if len(data)<args.top_n:
            n=len(data)
        else:
            n=args.top_n
        for num in range(n):
            print(f'{data[num][0]}: {data[num][1]}')

if __name__ == "__main__":
        main()
