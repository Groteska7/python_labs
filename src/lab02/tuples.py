import typing
import json
from ast import literal_eval as make_tuple

def format_record(rec: tuple[str, str, float]) -> str:
    # answer=[]
    FIO=list(rec[0].split())
    # answer.append(FIO[0])
    answer=FIO[0]+" "+FIO[1][0]
    # print(len(FIO))
    if len(FIO)==3:
        answer=answer+"."+(FIO[2][0])+"."
    return answer



print(format_record(make_tuple(input())))
