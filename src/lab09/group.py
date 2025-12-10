import csv
from dataclasses import dataclass
from pathlib import Path



from lab05.lib import r_csv
from lab08.models import Student

@dataclass
class Group:
    path: Path
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 

    # def _read_all(self):
    #     # TODO: реализовать чтение строк из csv 

    def list(self):
        group=r_csv(self.path)
        return group

    # def add(self, student: Student):
    #      # TODO: реализовать метод add()

    # def find(self, substr: str):
    #     # TODO: реализовать метод find()
    #     return [r for r in rows if substr in r["fio"]]  

    # def remove(self, fio: str):
    #     # TODO: реализовать метод remove()
    #     for i, r in enumerate(rows):
    #         if r["fio"] == fio:
    #             rows.pop(i)
    #             break

    # def update(self, fio: str, **fields):
    #     # TODO: реализовать метод update()

if __name__ == "__main__":
    group=Group("data/lab09/students.csv")
    mas = group.list()
    for student in mas:
        print(student.from_dict())