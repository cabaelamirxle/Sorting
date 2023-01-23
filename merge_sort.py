def mergeSort(num):
    if len(num) > 1:
        leftElem = num[:len(num)//2]
        rightElem = num[len(num)//2:]

        mergeSort(leftElem)
        mergeSort(rightElem)
        i = 0
        j = 0
        k = 0

        while i < len(leftElem) and j < len(rightElem):
            if leftElem[i] < rightElem[j]:
                num[k] = leftElem[i]
                i += 1
            else:
                num[k] = rightElem[j]
                j += 1
            k += 1

        while i < len(leftElem):
            num[k] = leftElem[i]
            i += 1
            k += 1

        while j < len(rightElem):
            num[k] = rightElem[j]
            j += 1
            k += 1
    
    print(num)

num = [32, 5, 85, 37, 38, 74, 18, 17, 19, 78]
mergeSort(num)
print(num)