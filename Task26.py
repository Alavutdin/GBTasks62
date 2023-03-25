'''Задача 26:  Напишите программу, которая на вход принимает два числа
 A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''
numberA = 3;
numberB = 5;

def integerPower (numberA, numberB):
    if numberA==numberB:
        return numberA
    return numberA**numberB
print(integerPower(numberA,numberB))

