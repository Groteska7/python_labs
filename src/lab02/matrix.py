import ast
import json
from typing import Union

def transpose(mat: list[list[float | int]]) -> list[list|int]:
    remat=[]
    reStr=[]
    if mat==[]:
        return mat
    a=len(mat[0])
    if not(all(len(mat[x])==a for x in range(len(mat)))):
        return "ValueError"
    for k in range(len(mat[0])):
        for i in mat:
            # print(i[k])
            reStr.append(i[k])
        remat.append(reStr)
        reStr=[]
    # print(reStr)
    return remat

def row_sums(mat: list[list[float | int]]) -> list[float|int]:
    a=len(mat[0])
    if not(all(len(mat[x])==a for x in range(len(mat)))):
        return "ValueError"
    string_sum=[]
    for string in mat:
        string_sum.append([sum(string)])
    return string_sum

def col_sums(mat: list[list[float | int]]) -> list[float]:
    a=len(mat[0])
    if not(all(len(mat[x])==a for x in range(len(mat)))):
        return "ValueError"
    column=[]
    reMat=[]
    for k in range(len(mat[0])):
        for i in mat:
            column.append(i[k])
        reMat.append(sum(column))
        column=[]
    return reMat



print("-------->",transpose(json.loads(input("transpose: "))))
print("-------->",row_sums(json.loads(input("row_sums: "))))
print("-------->",col_sums(json.loads(input("col_sums: "))))