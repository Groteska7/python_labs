from ast import literal_eval

def count_freq(tokens: list[str]) -> dict[str, int]:
    answ={}
    a=set(tokens)
    # print(a)
    for i in a:
        answ[i] = tokens.count(i)
    # print(answ["a"])
    return answ

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    answ=[]
    lvl_1={}
    keys=sorted(freq)
    for i in keys:
        lvl_1[i]=freq[i]
    # print("--->",lvl_1)
    # print(keys)
    answ=sorted(lvl_1.items(),reverse=True, key=lambda item: item[1])
    return answ


x=input().split()
print("count_freq: ",count_freq(x))
print("top_n: ",top_n(count_freq(x)))