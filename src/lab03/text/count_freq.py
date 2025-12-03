from ast import literal_eval

from .normalize import normalize_f

def count_freq_f(tokens: list[str]) -> dict[str, int]:
    tokens_normalize=[normalize_f(x) for x in tokens]
    answ={}
    a=sorted(tokens_normalize,reverse=True)
    # print(a)
    for i in a:
        answ[i] = tokens_normalize.count(i)
    # print(answ)
    return answ

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    k=0
    answ=[]
    lvl_1={}
    keys=sorted(freq)
    for i in keys:
        lvl_1[i]=freq[i]
        k+=1
    # print("--->",lvl_1)
    # print(keys)
    answ=sorted(lvl_1.items(),reverse=True, key=lambda item: item[1])
    return (answ[:min(n,k)])


# x=literal_eval(input())
# print("count_freq: ",count_freq_f(x))
# print("top_n: ",top_n(count_freq_f(x)))