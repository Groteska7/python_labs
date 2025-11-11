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
if enc=="":
    raise ValueError("Неверно указана кодировка файла")
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
    # print(f_names)
    mas.append(read_text(Path(A),enc))

total={}
for i in range(k):
    per={}
    work_str=mas[i]
    if work_str==None:
        break
    # print(work_str)
    # print(count_freq_f(tokenize_f(work_str)))
    # print(text_stats_f(work_str,False))
    # print(count_freq_f(tokenize_f(work_str)))
    per.update(count_freq_f(tokenize_f(work_str)))
    # print("per.items()-->",per.items())s
    total.update({(f_names[i],key): value for key, value in list(per.items())})
# print("total -------------->",total)
# print("per --------->",per)
flattened_rows=[]
for row in sorted(total.items(),reverse=True, key=lambda item: item[1]):
     flattened_row = list(row[0]) + [row[1]]
     flattened_rows.append(flattened_row)
# print(flattened_rows)
print("work_str ----->",work_str)
print("mas ---->",mas)
data_sum=""
for i in mas:
    data_sum+="".join(i)
    if i!=mas[-1]:
        data_sum+=" "
print("data_sum ----->",data_sum)
write_csv(top_n(count_freq_f(tokenize_f(data_sum))),"data/lab04/report_total.csv",("word","count"))
write_csv(flattened_rows,"data/lab04/report_per_file.csv",("file","word","count"))