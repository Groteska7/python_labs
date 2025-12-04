import sys
from src.lab03.text.normalize import normalize_f
from src.lab03.text.tokenize import tokenize_f
from src.lab03.text.count_freq import count_freq_f, top_n


def text_stats_f(inp: str, flag: bool) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    mas = tokenize_f(normalize_f(inp))
    # inp=normalize(inp,1,1)
    # print(inp)
    if flag:
        par_1 = max([len(x) for x in mas])
        # print(par_1)
        # print(par_1)
        # print(top_n(count_freq(inp.lower().split()))[0][0])
        if par_1 > 5:
            print("слово", " " * abs(par_1 - 5), "|", "частота")
        elif par_1 < 5:
            print("слово", " |", "частота")
            par_1 = 5
        print("-" * (par_1 + abs(par_1 - 5) + 3))
        # print(tokenize(inp))
        n = 5
        x = 0
        if len(top_n(count_freq_f(mas))) < 5:
            n = len(top_n(count_freq_f(mas)))
        for i in top_n(count_freq_f(mas)):
            if x == n:
                break
            print(f'{i[0]} {" "*(par_1-len(i[0]))} | {i[1]}')
            x += 1
    else:
        print("Топ 5:")
        x = 0
        n = 5
        if len(top_n(count_freq_f(mas))) < 5:
            n = len(top_n(count_freq_f(mas)))
        while x < n:
            i = top_n(count_freq_f(mas))[x]
            print(f'{i[0]}: {i[1]}')
            x += 1


# # text_stats(sys.stdin.read().split())
# print("введите True/False чтобы включить/выключить табличный режим")
# key=input()
# for line in sys.stdin:
#     text_stats_f(normalize_f(line,1,1),key)


def text_stats_f_t2(inp: str, flag: bool) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    mas = tokenize_f(normalize_f(inp))
    # inp=normalize(inp,1,1)
    # print(inp)
    if flag:
        par_1 = max([len(x) for x in mas])
        # print(par_1)
        # print(par_1)
        # print(top_n(count_freq(inp.lower().split()))[0][0])
        if par_1 > 4:
            print("файл", "    ", "|", "слово", " " * abs(par_1 - 4), "|", "частота")
        elif par_1 < 4:
            print("файл", "    ", "|", "слово", "|", "частота")
            par_1 = 4
        print("-" * (par_1 + abs(par_1 - 5) + 3 + 8))
        # print(tokenize(inp))
        n = 5
        x = 0
        if len(top_n(count_freq_f(mas))) < 5:
            n = len(top_n(count_freq_f(mas)))
        for i in top_n(count_freq_f(mas)):
            if x == n:
                break
            print(f' | {i[0]} {" "*(par_1-len(i[0]))} | {i[1]}')
            x += 1
    else:
        print("Топ 5:")
        x = 0
        n = 5
        if len(top_n(count_freq_f(mas))) < 5:
            n = len(top_n(count_freq_f(mas)))
        while x < n:
            i = top_n(count_freq_f(mas))[x]
            print(f'{i[0]}: {i[1]}')
            x += 1
