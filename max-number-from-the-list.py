def maximum(x=[]):
    maxNum = 0
    for i in x:
        if i > maxNum:
            maxNum = i
    return maxNum


print(maximum([13, 3, 200, 5, 4, 45]))
