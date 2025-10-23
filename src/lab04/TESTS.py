# import sys
# from pathlib import Path
# PROJECT_ROOT = Path(__file__).parent.parent
# sys.path.insert(0, str(PROJECT_ROOT))
from io_text_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(txt)
res=write_csv([("word","count"),("test",3)], "data/lab04/check.csv",["one","two"])