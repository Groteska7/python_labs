import sys
from text.count_freq import top_n
from text.count_freq import count_freq
from text.normalize import normalize
from text.tokenize import tokenize


def text_stats(inp: str, flag: str) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    mas=tokenize(normalize(inp))
    # inp=normalize(inp,1,1)
    # print(inp)
    if flag=="True":
        par_1=max([len(x) for x in mas])
        print(par_1)
        # print(par_1)
        # print(top_n(count_freq(inp.lower().split()))[0][0])
        if par_1>5:
            print("слово"," "*abs(par_1-5),"|","частота")
        elif par_1<5:
            print("слово"," |","частота")
            par_1=5
        print("-"*(par_1+abs(par_1-5)+10))
        # print(tokenize(inp))
        n=5
        x=0
        if len(top_n(count_freq(mas)))<5:
            n=len(top_n(count_freq(mas)))
        for i in top_n(count_freq(mas)):
            if x==n:
                break
            print(f'{i[0]} {" "*(par_1-len(i[0]))} | {i[1]}')
            x+=1
    else:
        print("Топ 5:")
        x=0
        n=5
        if len(top_n(count_freq(mas)))<5:
            n=len(top_n(count_freq(mas)))
        while x<n:
            i=top_n(count_freq(mas))[x]
            print(f'{i[0]}: {i[1]}')
            x+=1

# text_stats(sys.stdin.read().split())
print("введите True/False чтобы включить/выключить табличный режим")
key=input()
for line in sys.stdin:
    text_stats(normalize(line,1,1),key)