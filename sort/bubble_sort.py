from random import shuffle

l = [i for i in range(10)]
shuffle(l)
print(l)


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1, i, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]


bubble_sort(l)

print(l)
