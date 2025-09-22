def min_max(IN_string):
    work_mas=[]
    if len(IN_string)==0:
        print("ValueError")
    if all([str(x) in "0123456789" for x in IN_string.split()]):
        for x in IN_string.split():
            if x.find("."):
                work_mas.append(float(x))
            else:
                work_mas.append(int(x))
    else:
        print("TypeError")
    return work_mas
IN_string=input("строкой через пробел: ")
print(min_max(IN_string))