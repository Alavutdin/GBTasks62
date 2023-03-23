'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
второго множества. Затем пользователь вводит сами элементы множеств.'''

mol = [int(x) for x in input().split()]
numberOne = mol[0]
numberTwo = mol[1]
setOne = set()
setTwo = set()
listOne = list()
numberA=[int(x) for x in input().split()]
numberK=set(numberA)
for i in numberK:
    setOne.add(i)
numberB = [int(x) for x in input().split()]
numberKOne =set(numberB)
for i in numberKOne:
    setTwo.add(i)
lok = setOne & setTwo
kool =list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
