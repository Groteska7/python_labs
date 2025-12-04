from typing import Union
import json
import ast


def min_max(input_data: list[int | float]) -> list[int | float]:
    # print(input_data)
    if input_data == []:
        return "ValueError"
    # if all([str(x) in "0123456789" for x in IN_string.split()]):
    #    for x in IN_string.split():
    #        if x.find("."):
    #            work_mas.append(float(x))
    #        else:
    #            work_mas.append(int(x))
    else:
        return min(input_data), max(input_data)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    answ = []
    for i in mat:
        for j in i:
            if str(j) in "0123456789":
                answ.append(j)
            else:
                return "TypeError"
    return answ


print("-------------------------------->", min_max(json.loads(input("min_max: "))))
# print(min_max([int(float(x)) if float(x)%1==0  else float(x) for x in input().split()]))

print(
    "-------------------------------->",
    unique_sorted(json.loads(input("nique_sorted: "))),
)
# print(unique_sorted([int(float(x)) if float(x)%1==0  else float(x) for x in input().split()]))

print(
    "-------------------------------->", flatten(ast.literal_eval(input("flatten: ")))
)
