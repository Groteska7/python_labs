import typing
from ast import literal_eval

def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec)!=3:
        return "ValueError"
    if not all([type(rec[0])==str,type(rec[1])==str,type(rec[2])==float]):
        return "TypeError"
    # answer=[]
    FIO=list(rec[0].split())
    # answer.append(FIO[0])
    answer=str(FIO[0]).title()+" "+str(FIO[1][0]).upper()
    # print(len(FIO))
    if len(FIO)==3:
        answer=answer+"."+str(FIO[2][0]).upper()+"., "
    else:
        answer+="., "
    answer=answer+"гр. "+rec[1]+", "+"GPA "+f'{str(round(rec[-1],2)):04}'
    return answer


inTuple=str(input("format_record: "))
if inTuple=="":
    print("ValueError")
else:
    print(format_record(literal_eval(inTuple)))
