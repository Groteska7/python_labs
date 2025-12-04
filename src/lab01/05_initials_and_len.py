name, fam, otch = map(str, input("ФИО: ").split())
print(f"ФИО: {name[0].upper()+fam[0].upper()+otch[0].upper()}.")
print(f'Длина (символов): {len(name)+len(fam)+len(otch)+2}')
