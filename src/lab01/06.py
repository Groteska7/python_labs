n = int(input())
och = []
zoch = []
for i in range(n):
    name, fam, age, form = map(str, input().split())
    inf = name + " " + fam + " " + age
    if form == "True":
        och.append(inf)
    else:
        zoch.append(inf)
print(len(och), len(zoch))
