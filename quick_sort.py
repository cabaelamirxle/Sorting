def quickSort(num):
    length = len(num)
    if length <= 1:
        return num
    else:
        pivot = num.pop()

    higher = []
    lower = []

    for item in num:
        if item > pivot:
            higher.append(item)
        
        else:
            lower.append(item)

    print(num)
    return quickSort(lower) + [pivot] + quickSort(higher)

num = num = [32, 5, 85, 37, 38, 74, 18, 17, 19, 78]
print(quickSort(num))