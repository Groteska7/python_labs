from normalize import normalize
import re
def tokenize(text: str) -> list[str]:
    normalize(text)
    mas=re.split(r'\W+|\s+',text)
    return mas
print(tokenize(input()))