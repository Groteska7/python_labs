import sys
from text.count_freq import top_n
from text.count_freq import count_freq


def text_stats(inp: str) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    print("Топ 5:")
    for i in top_n(count_freq(inp.split())):
        print(f'{i[0]}: {i[1]}')

# text_stats(sys.stdin.read().split())
for line in sys.stdin:
    text_stats(line)
