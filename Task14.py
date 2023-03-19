
"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N."""

N = abs(int(input('Введите число N ')))
number_stop = 0
P = 2
for i in range(N):
    if number_stop != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            number_stop = 1
    else:
        i = N