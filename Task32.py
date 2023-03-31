"""Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)"""

list_one = [9, 2, 5, 6, 8, 6, 1, 8, 7]
number_min = int(input())
number_max = int(input())
for i in range(len(list_one)):
    if number_min<=list_one[i]<=number_max:
        print(i)