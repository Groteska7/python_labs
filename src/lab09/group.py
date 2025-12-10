import csv
from dataclasses import dataclass
from pathlib import Path

from lab05.lib import r_csv
from lab08.models import Student




@dataclass
class Group:
    head=["fio", "birthdate", "group", "gpa"]
    path: Path
    def _ensure_storage_exists(self):
        self.path.write_text("", encoding="utf-8",newline="")
        with self.path.open("w",encoding="utf-8",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.head)

    def __init__(self, storage_path: str):
        try:
            self.path = Path(storage_path)
        except:
            raise ValueError("Указанный путь не путь, видимо.")
        if not self.path.exists():
            self._ensure_storage_exists()
            print("Указанный файл не имел заголовок!")

    def _read_all(self):
        all=r_csv(self.path)
        group=[]
        for student in all:
            group.append(Student.from_dict(student))
        return group

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        # print(student)
        # print(student.fio,student.birthdate,student.group,student.gpa)
        with open(self.path, "a",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return print(f"студент {student.fio} добавлен")
    
    def find(self, substr: str):
        # print("---------------->",group._read_all())
        rows=[]
        for student in self._read_all():
            rows.append(Student.to_dict(student))
        # print("====================>",rows)
        find_s=[r for r in rows if substr in r["fio"]] 
        if find_s==[]:
            return f"{substr} not found"
        else:
            return find_s

    def remove(self, fio: str):
        if self.find(fio) ==  f"{fio} not found":
            return f"{fio} not found"
        else: fio = self.find(fio)[0]["fio"]
        # print(fio)
        students=self._read_all()
        clean_file=[r for r in students if r.fio != fio] 
        with open(self.path, "w",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(self.head)
            for student in clean_file:
                writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return f"Студент {fio} удален (отчислен)"
        

        # for i, r in enumerate(rows):
        #     if r["fio"] == fio:
        #         rows.pop(i)
        #         break

    def update(self, fio: str, **fields):
        if self.find(fio) ==  f"{fio} not found":
            return f"{fio} not found"
        else: fio = self.find(fio)[0]["fio"]
        students=self._read_all()
        # print(students)
        for s in students:
            if s.fio==fio:
                for key, data in fields.items():
                    setattr(s,key,data) #Записывает в Student в значение KEY данные из DATA
                break
        # print(students)
        with open(self.path, "w",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(self.head)
            for student in students:
                writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return f"информация {list(fields.keys())} о cтуденте {fio} изменена"

if __name__ == "__main__":
    student=Student(
        fio = "Юля Роуз Семенова",
        birthdate = "11.11.2011",
        group = "KRUTAYA-01-1",
        gpa = 5.0
    )
    group=Group("data/lab09/students.csv")

    #--------------> Проверка работоспособности list
    print("list test --------->",group.list(),"<---------")
    #--------------> Проверка работоспособности _read_all
    print("_read_all test --------->",group._read_all(),"<---------")
    print()
    #--------------> Проверка работоспособности add
    group.add(student=student)
    #--------------> Проверка работоспособности find
    print(group.find("Юля"))
    #--------------> Проверка работоспособности remove
    print(group.remove("Юля"))
    #--------------> Проверка работоспособности update
    print(group.update("Фантазий Закончивич",group = "GGGGGGGGGGGGG-1-1"))