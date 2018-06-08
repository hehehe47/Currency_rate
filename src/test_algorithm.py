import random


# 冒泡排序

def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [3, 4, 1, 2, 6, 2, 3, 4]
bubble_sort(l)
print(l)
