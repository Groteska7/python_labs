import typing
import json
from ast import literal_eval as make_tuple

def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec)!=3:
        return "ValueError"
    if not all([type(rec[0])==str,type(rec[1])==str,type(rec[2])==float]):
        return "TypeError"
    # answer=[]
    FIO=list(rec[0].split())
    # answer.append(FIO[0])
    answer=FIO[0]+" "+FIO[1][0]
    # print(len(FIO))
    if len(FIO)==3:
        answer=answer+"."+(FIO[2][0])+"., "
    else:
        answer+="., "
    answer=answer+rec[1]+", "+"GPA "+f'{str(round(rec[-1],2)):04}'
    return answer



print(format_record(make_tuple(input("format_record: "))))
