"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть"""

number = int(input("Введите количество монет: "))
number_zero =0
number_one =0
for i in range(number):
    x = int(input("Введите монеты решкой 0, гербом 1: "))
    if x==0:
        number_zero+=1
    else:
        number_one+=1
if (number_one>number_zero):
    print(number_zero)
else:
    print(number_one)