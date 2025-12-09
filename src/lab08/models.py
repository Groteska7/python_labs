from dataclasses import dataclass
from datetime import date, datetime



@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
#Валидация birthdate <-----------------------------------------------
        if not self.birthdate or self.birthdate=="" or self.birthdate== None:
            raise ValueError("Строка birthdate не должна быть пустой")
        if not self.fio or self.fio =="" or self.fio == None:
            raise ValueError("Строка fio не должна быть пустой")
        if not self.group or self.group =="" or self.group == None:
            raise ValueError("Строка group не должна быть пустой")
        try:
            life_years = datetime.strptime(self.birthdate, "%d.%m.%Y").date()
            
            if life_years > date.today():
                raise ValueError("Данная программа для пользователей старше нуля лет")
            
            if (date.today() - life_years).days / 365 > 200:
                raise ValueError("Не прокатило.. попробуй еще, алеутский морской окунь")
            
            # return life_years
        except ValueError as errors:
            if "does not match format" in str(errors):
                raise ValueError(
                    f"Неверный формат даты: {self.birthdate}. "
                    f"Ожидается формат DD.MM.YYYY"
                ) from errors
#Валидация GPA <-----------------------------------------------------
        if not self.gpa or self.gpa=="" or self.gpa== None:
            raise ValueError("Строка GPA не должна быть пустой")
        # print("----------------------->",self.age)
        self.gpa=float(self.gpa)
        if type(self.gpa)!=float:
            raise ValueError (
                "GPA должен быть числом"
                )
        if not (0 <= self.gpa <= 5):
            raise ValueError(
                f"Средний балл должен быть в диапазоне от 0 до 5, "
            )
        

    def age(self) -> int:
        # print(self.birthdate)
        birth_date = datetime.strptime(self.birthdate, "%d.%m.%Y").date()
        age = date.today().year - birth_date.year
        today = date.today()

        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        if not self.fio:
            raise ValueError("Строка fio не должна быть пустой")
        if not self.group:
            raise ValueError("Строка group не должна быть пустой")
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio= d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa = d["gpa"]
        )

    def __str__(self):
        return f"ВЫ, {self.fio}, студент группы {self.group}, {self.age()}, Так еще и учитесь на {self.gpa}"

if __name__ == "__main__":
    data = Student(
        fio="Вован Вакакойстудент Вовович",
        birthdate="25.01.2007",
        group="KRUT-99-1",
        gpa=4.5
    )
    print(data)
    print(f"Словарь: {data.to_dict()}") 