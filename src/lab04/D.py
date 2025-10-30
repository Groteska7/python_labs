from io_text_csv import read_text, write_csv, frequencies_from_text,sorted_word_counts
import csv
from pathlib import Path
import sys

# PROJECT_ROOT = Path(__file__).parent.parent.parent
# sys.path.insert(0, str(PROJECT_ROOT))

# from src.lab03.text.normalize import normalize_f
from src.lab03.text.tokenize import tokenize_f
from src.lab03.text.count_freq import count_freq_f, top_n
from src.lab03.text_stats import text_stats_f

enc=input("введите кодировку: ")
try:
    k=int(input("введите количество файлов: "))
except ValueError:
    print("Неправильно указано количество файлов") 
    exit()
# if type(k)!="int":
#     raise TypeError("Неправильно указано количество файлов")
mas=[]
f_names=[]
for i in range(k):
    # mas=mas.append(read_text(Path(input((f"введите путь к  файлу {i}: ")))))
    A=input(f"введите путь к  файлу {i+1}: ")
    f_names.append(A.split("/")[-1])
    print(f_names)
    mas.append(read_text(Path(A),enc))
# print(mas)
per={}
total={}
for i in range(k):
    work_str=mas[i]
    if work_str==None:
        break
    # print(work_str)
    # print(count_freq_f(tokenize_f(work_str)))
    # print(text_stats_f(work_str,False))
    # print(count_freq_f(tokenize_f(work_str)))
    per.update(count_freq_f(tokenize_f(work_str)))
    total.update({f"{f_names[i]},{key}": value for key, value in per.items()})
    # print(total)
# print(per)
write_csv(top_n(count_freq_f(tokenize_f(work_str))),"data/lab04/report_per_file.csv",("word","count"))
write_csv((sorted(total.items(),reverse=True, key=lambda item: item[1])),"data/lab04/report_total.csv",("file","word","count"))