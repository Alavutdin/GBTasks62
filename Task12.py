"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S
 и их произведение P. Помогите Кате отгадать задуманные Петей числа."""

numberA = abs(int(input('Введите первое натуральное число X ')))
numberB = abs(int(input('Введите второе натуральное число Y ')))
S = numberA + numberB
P = numberA * numberB
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)