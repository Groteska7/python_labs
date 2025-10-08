def normalize(text: str, casefold: bool = True, yo2e: bool = True) -> str:
    lvl_1=""
    answ=""
    print("----->",text)
    if yo2e:
        text=text.replace("ё","е").replace("Ё","Е")
    text=text.replace("\\t"," ").replace("\\r"," ").replace("\\n"," ")
    for i in text.split():
        lvl_1+=str(i)+" "
    lvl_1=lvl_1[:-1]
    print("--------->",lvl_1)
    if casefold:
        for x in lvl_1:
            answ+=x.lower()
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
# print(a)
# print("|"+normalize(a,casefold=C,yo2e=Y)+"|")
          
