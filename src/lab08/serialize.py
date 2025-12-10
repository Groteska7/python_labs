import json
from models import Student
from pathlib import Path


def students_to_json(students, path: Path):
    data = [s.to_dict() for s in students]
    # print(data)
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except IOError as e:
        raise IOError(f"Ошибка при записи файла: {e}")

def students_from_json(path: Path):
    path=Path(path)
    if path.suffix != ".json":
        raise TypeError("Неверное расширение файла")
    try:
        with open(path,'r',encoding="utf-8") as file:
            data=json.load(file)
    except FileNotFoundError:                                                   
        raise ValueError("Файл не найден")

    if not isinstance(data,list):
        raise ValueError("Файл должен содержать список")
    
    students=[]
    # print(data)
    for item in data:
        # print("----------------------------->",item)
        if not isinstance(item,dict):
            raise ValueError("Файл должен содержать список СЛОВАРЕЙ")
        student = Student.from_dict(item)
        students.append(student)
        
    # print(students)
    return students
    
if __name__ == "__main__":
    input_path = "data/lab08/students_input.json"
    output_path = "data/lab08/students_output.json"

    # with open(input_path,"r",encoding="utf-8") as file:
    #     data=json.load(file)
    for x in students_from_json(input_path):
        print(x)
    data=students_from_json(input_path)
    students_to_json(data,output_path)
