import random


# 冒泡排序

def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def bubble_sort2(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


import time

l = sorted([random.randint(0, 10000) for i in range(10000)])
t1 = time.time()
bubble_sort2(l)
t2 = time.time()
# print(l)
print(t2 - t1)
