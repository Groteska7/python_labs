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

line=Path(input("введите путь к файлу: "))
work_str=read_text(line)
# print(work_str)
print(text_stats_f(work_str,True))
write_csv(top_n(count_freq_f(tokenize_f(work_str))),"data/lab04/report.csv",("word","count"))
