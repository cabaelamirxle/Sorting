def selectionsorting(num):

    for i in range (0, len(num) - 1):
        minpos = i
        for j in range (i + 1, len(num)):
            if num[j] < num[minpos]:
                minpos = j

        num[i], num[minpos] = num[minpos], num[i]

        print(num)

num = [32, 5, 85, 37, 38, 74, 18, 17, 19, 78]
selectionsorting(num)
print(num) 