from ast import literal_eval
import sys
def normalize_f(text: str, casefold: bool = True, yo2e: bool = True) -> str:
    lvl_1=""
    answ=""
    # print("----->",text)
    if yo2e:
        text=text.replace("ё","е").replace("Ё","Е")
    text=text.replace("\\t"," ").replace("\\r"," ").replace("\\n"," ").replace('"',"").replace("'","")
    # print(text.split())
    lvl_1=" ".join(text.split())
    # lvl_1=[x.join(" ")for x in lvl_1.split()]
    # print("--------->",lvl_1)
    if casefold:
        for x in lvl_1:
            answ+=x.casefold()
        return answ
    else:
        return lvl_1

# a=input()
# C=bool(input("casefold: "))
# if C=="":
#     C=1
# Y=bool(input("yo2e: "))
# if Y=="":
#     Y=1
# # print(a)
# print("|"+normalize_f(a,casefold=C,yo2e=Y)+"|")

# print("casefold | yo2e | string")
# for line in sys.stdin:
#     C,Y,a=line.split()
#     print("|"+normalize_f(a,casefold=bool(C),yo2e=bool(Y))+"|")