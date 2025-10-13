from normalize import normalize
import re
from ast import literal_eval
def tokenize(text: str) -> list[str]:
    text=normalize(text)
    print(text)
    mas=re.findall(r'\w+\-\w+|\w+',text)
    answ=[x for x in mas if x!="" and x!=None]
    # print(mas)
    return answ
# print(tokenize(literal_eval(input())))