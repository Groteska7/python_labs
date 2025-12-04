from .normalize import normalize_f
import re
from ast import literal_eval


def tokenize_f(text: str) -> list[str]:
    text = normalize_f(text)
    # print(text)
    mas = re.findall(r'\w+\-\w+|\w+', text)
    answ = [x for x in mas if x != "" and x != None]
    # print(mas)
    return answ


# print(tokenize(literal_eval(input())))
