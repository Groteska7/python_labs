def min_max(input_data: list[int,float]) -> tuple[float | int, float | int]:
    if input_data==[]:
        return "ValueError"
    #if all([str(x) in "0123456789" for x in IN_string.split()]):
    #    for x in IN_string.split():
    #        if x.find("."):
    #            work_mas.append(float(x))
    #        else:
    #            work_mas.append(int(x))
    else:
        return input_data.sort()

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print(min_max(input().split()))
print(unique_sorted(input().split()))