'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму
двух целых неотрицательных чисел. Из всех арифметических операций допускаются
только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4 '''

numberA=int(input("Введите целое неотрицательное число а :"))
numberB=int(input("Введите целое неотрицательное число b :"))
def sum(numberA,numberB):
    if numberB==0:
        return numberA
    return 1+sum(numberA,numberB-1)

print(sum(numberA,numberB))