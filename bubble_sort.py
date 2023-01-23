def sort(num):
    for i in range(len(num) -1, 0, -1):
        for j in range (i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

        print(num)

num = [32, 5, 85, 37, 38, 74, 18, 17, 19, 78]
sort(num)
print(num)