def insertionsort(num):
    for i in range(1, len(num)):
        element = num[i]
        j = i - 1
        while j >= 0 and element < num[j]:
            num[j + 1] = num[j]
            j -= 1
            num[j + 1] = element

        print(num)

num = [32, 5, 85, 37, 38, 74, 18, 17, 19, 78]
insertionsort(num)
print(num)