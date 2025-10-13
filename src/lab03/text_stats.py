import sys
from text.count_freq import top_n
from text.count_freq import count_freq
from text.normalize import normalize


def text_stats(inp: str, flag: bool) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    if flag==True:
        par_1=max([len(x) for x in inp.split()])
        print(par_1)
        # print(par_1)
        # print(top_n(count_freq(inp.lower().split()))[0][0])
        if par_1>5:
            print("слово"," "*abs(par_1-5),"|","частота")
        elif par_1<5:
            print("слово"," |","частота")
            par_1=5
        print("-"*(par_1+abs(par_1-5)+10))
        for i in top_n(count_freq(inp.lower().split())):
            print(f'{i[0]} {" "*(par_1-len(i[0]))} | {i[1]}')
    elif flag==False:
        print("Топ 5:")
        x=0
        while x<5:
            i=top_n(count_freq(inp.split()))[x]
            print(f'{i[0]}: {i[1]}')
            x+1

# text_stats(sys.stdin.read().split())
print("введите True/False чтобы включить/выключить табличный режим")
key=bool(input())
for line in sys.stdin:
    text_stats(normalize(line),key)