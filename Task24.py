'''Дан массив. Найдите три последовательных элемента в массиве,
* сумма которых максимальна'''

number = int (input())
array =list()
for i in range(number):
    x=int(input())
    array.append(x)
array_count = list()
for i in range(len(array)-1):
    array_count.append(array[i-1]+array[i]+array[i+1])
array_count.append(array[-2]+array[-1]+array[0])
print(max(array_count))